import datetime
import multiprocessing
import os
import re
import time

import click
from flask import current_app
from flask.cli import with_appcontext
from jinja2 import Environment, FileSystemLoader
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

from dh_potluck.audit_log.models import Operation
from dh_potluck.utils import get_db

template_dir = os.path.join(os.path.dirname(__file__), 'trigger_templates')
jinja_env = Environment(loader=FileSystemLoader(template_dir))


class RetriesExceededError(Exception):
    pass


def echo(message):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    click.echo(f'[{timestamp}] {message}')


def execute_query(query, queue, database_uri):
    try:
        # Create a dedicated connection for each query so they can easily be killed
        engine = create_engine(database_uri)
        conn = engine.connect()

        # Pass the MySQL connection ID to the parent process so it can kill the query if necessary
        queue.put(conn.connection.thread_id())
        conn.execute(query)
    except Exception as e:
        # Pass exceptions to the parent process so they can be re-raised there
        queue.put(e)


def execute_with_timeout(query):
    ctx = click.get_current_context()
    timeout = ctx.obj['timeout']
    sleep = ctx.obj['sleep']
    max_retries = ctx.obj['max_retries']

    attempts = 0
    while attempts < max_retries:
        # Execute the query in a subprocess so we can easily kill if it runs too long
        queue = multiprocessing.Queue()
        p = multiprocessing.Process(
            target=execute_query, args=(query, queue, current_app.config['SQLALCHEMY_DATABASE_URI'])
        )
        p.start()

        # Wait for up to n seconds for the query to finish
        p.join(timeout)

        # If after n seconds it's still alive, we need to kill it
        if p.is_alive():
            first_line_of_query = query.split('\n')[0]
            echo(
                f'Query "{first_line_of_query}" exceeded {timeout} seconds execution time. '
                f'Terminating it then waiting {sleep} seconds until retry. '
                f'[Attempt {attempts + 1}/{max_retries}]'
            )
            connection_id = queue.get()
            p.kill()
            get_db().session.execute(f'KILL {connection_id}')
            time.sleep(sleep)
            attempts += 1
        else:
            # If it's finished, check for any exceptions and re-raise them.
            for _ in range(queue.qsize()):
                result = queue.get()
                if isinstance(result, Exception):
                    raise result

            # Otherwise, query executed successfully
            return

    raise RetriesExceededError()


def drop_trigger(trigger_name):
    try:
        echo(f'Dropping {trigger_name} trigger...')
        execute_with_timeout(text(f'DROP TRIGGER {trigger_name}'))
        echo(f'Dropped {trigger_name} trigger.')
    except OperationalError as e:
        if "(1360, 'Trigger does not exist')" in str(e):
            echo(f'No trigger {trigger_name} exists, moving on.')
            return False
        raise e
    return True


def create_or_replace_trigger(trigger_name, trigger_sql):
    try:
        result = get_db().session.execute(text(f'SHOW CREATE TRIGGER {trigger_name}'))
        original_trigger_sql = result.mappings().first()['SQL Original Statement']
    except OperationalError as e:
        if "(1360, 'Trigger does not exist')" in str(e):
            # Create trigger
            echo(f'Creating {trigger_name} trigger...')
            execute_with_timeout(text(trigger_sql))
            echo(f'Created {trigger_name} trigger.')
            return
        raise e

    # Strip out DEFINER argument, so we can compare the two triggers
    # The DEFINER clause is automatically added by MySQL when creating triggers, and defaults
    # to the user who executes the CREATE TRIGGER statement.
    original_trigger_sql = re.sub(r' DEFINER[^\s]+', '', original_trigger_sql)

    if original_trigger_sql == trigger_sql:
        echo(f'No changes to {trigger_name} trigger required.')
    else:
        echo(f'Replacing {trigger_name} trigger...')
        execute_with_timeout(text(f'DROP TRIGGER {trigger_name}'))
        execute_with_timeout(text(trigger_sql))
        echo(f'Replaced {trigger_name} trigger.')


def get_trigger_name(table_name, operation):
    return f'audit_{table_name}_{operation.value}s'


@click.group(help='Manage audit logging triggers.', name='audit-log')
@click.option(
    '--timeout',
    default=2,
    type=int,
    help='Number of seconds to wait before killing CREATE or DROP TRIGGER queries.',
)
@click.option(
    '--sleep',
    default=5,
    type=int,
    help='Number of seconds to wait before retrying CREATE or DROP TRIGGER queries.',
)
@click.option(
    '--max-retries',
    default=10,
    type=int,
    help='Number of times to retry killed CREATE or DROP TRIGGER queries.',
)
@click.pass_context
def audit_log(ctx, timeout, sleep, max_retries):
    ctx.ensure_object(dict)
    ctx.obj['timeout'] = timeout
    ctx.obj['sleep'] = sleep
    ctx.obj['max_retries'] = max_retries


@audit_log.command(help='Sync (and enable) all MySQL triggers used for managing the audit logs.')
@with_appcontext
def sync_triggers():
    ctx = click.get_current_context()
    models = [mapper.class_ for mapper in get_db().Model.registry.mappers if mapper.class_]

    for model in models:
        table_name = model.__table__.name

        try:
            if getattr(model, '__audit_log__', False):
                column_names = [column.name for column in model.__table__.columns]

                for operation in Operation:
                    trigger_name = get_trigger_name(table_name, operation)
                    trigger_sql = jinja_env.get_template(f'audit_{operation.value}s.jinja2').render(
                        trigger_name=trigger_name,
                        table_name=table_name,
                        column_names=column_names,
                    )
                    create_or_replace_trigger(trigger_name=trigger_name, trigger_sql=trigger_sql)

            else:
                for operation in Operation:
                    drop_trigger(get_trigger_name(table_name, operation))

        except RetriesExceededError:
            echo(
                f'Exceeded {ctx.obj["max_retries"]} retries attempting to modify triggers for '
                f'table "{table_name}". Try running again later or with different parameters.'
            )


@audit_log.command(help='Drop all MySQL triggers used for managing the audit logs.')
@with_appcontext
def drop_triggers():
    ctx = click.get_current_context()
    for table_name in get_db().engine.table_names():
        try:
            for operation in Operation:
                drop_trigger(get_trigger_name(table_name, operation))
        except RetriesExceededError:
            echo(
                f'Exceeded {ctx.obj["max_retries"]} retries attempting to drop triggers for '
                f'table "{table_name}". Try running again later or with different parameters.'
            )
