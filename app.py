# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 11:54:15 2020

@author: Shafiullah Noorbasha
This is the entry point for python recommendation engine.
"""

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

class HelloWorld1(Resource):
    def ping(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld1, '/ping')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


