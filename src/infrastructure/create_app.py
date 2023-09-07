"""
Creates the flask app that will be runned 
"""

from flask import Flask 


def create_app():
    app = Flask(__name__)
    from .blueprints.collector.collector_blueprint import