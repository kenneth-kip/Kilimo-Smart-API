"""" Manage.py """

import os
import unittest

from flask import url_for
from flask.cli import with_appcontext

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db
from app.main.models import produce, price, region

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@app.cli.command()
def list_routes():
    """ Lists all the routes. """
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.parse.unquote(
            "{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)
    for line in sorted(output):
        print(line)


@app.shell_context_processor
def dbshell():
    return {
        'db': db,
        'Region': region.Region,
        'Price': price.Price,
        'Produce': produce.Produce
    }


@app.cli.command()
def create_db():
    """Creates the db tables."""
    db.create_all()


@app.cli.command()
def drop_db():
    """Drops the db tables."""
    db.drop_all()
