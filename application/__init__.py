import os
import importlib

INSTALLED_APPS = (
    'home',
)

def register_applications(flask_app):
    for package_name in INSTALLED_APPS:
        import_app = importlib.import_module('.' + package_name, __package__)
        print(import_app.URL_PREFIX)
        flask_app.register_blueprint(import_app.BP, url_prefix=import_app.URL_PREFIX)
