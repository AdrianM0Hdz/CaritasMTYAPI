from flask import Blueprint, Response, request, jsonify

ticket_blueprint = Blueprint('ticket_blueprint', __name__)

@ticket_blueprint.route("/<string:id>", methods=["GET"])
def get_ticket_by_id_handler(id: str):
    
    return jsonify()
