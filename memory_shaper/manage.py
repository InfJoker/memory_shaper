import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db, get_config_object_name

app.config.from_object(get_config_object_name(os.environ['APP_ENVIRONMENT']))

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
