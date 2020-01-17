from flask import request, current_app
from flask_restful import Resource

class Hello(Resource):
    def get(self):
        print('test')
        # 返回所有数据
        return 'home, flask'
