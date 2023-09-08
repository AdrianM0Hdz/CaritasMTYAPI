"""
Creates the flask app that will be runned 
"""

from flask import Flask 

def create_app() -> Flask:
    app = Flask(__name__)
    
    from .blueprints.collector.collector_blueprint import collector_blueprint
    app.register_blueprint(collector_blueprint, url_prefix="/collector")
    
    from .blueprints.manager.manager_blueprint import manager_blueprint
    app.register_blueprint(manager_blueprint, url_prefix="/manager")

    from .blueprints.ticket.ticket_blueprint import ticket_blueprint
    app.register_blueprint(ticket_blueprint, url_prefix='/ticket')

    return app