"""
Creates the flask app that will be runned 
"""

from flask import Flask 

def create_app() -> Flask:
    app = Flask(__name__)
    
    from .blueprints.collector.collector_blueprint import collector_blueprint
    app.register_blueprint(collector_blueprint, url_prefix="/collector")
    
    return app