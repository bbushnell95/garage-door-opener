""" Copyright Brett Bushnell 2018 """
from flask import request
from flask_restful import Resource

class Home(Resource):
    def get(self):
        return 'Sorry! We are under construction!'
