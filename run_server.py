from flask import Flask
from application import register_applications
from database import db

ENV = "development"


def after_create_app(func):
    def wrapper(*args, **kwargs):
        app = func(*args, **kwargs)
        db.init_app(app)
        return app
    return wrapper


@after_create_app
def create_app(py_config_file):
    app = Flask(__name__)
    app.config.update(ENV=ENV)
    app.config.from_pyfile(py_config_file)
    register_applications(app)
    return app


if __name__ == '__main__':
    my_app = create_app('config/%s.py' % ENV)
    my_app.run()
