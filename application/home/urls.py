from .controller import Hello
from flask import Blueprint
from flask_restful import Api

BP = Blueprint('home', __name__)
api = Api(BP)


api.add_resource(Hello, '/hello/')

