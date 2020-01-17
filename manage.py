from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager
from run_server import create_app, ENV
from application.home import model
from database import db

app = create_app('config/%s.py' % ENV)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
