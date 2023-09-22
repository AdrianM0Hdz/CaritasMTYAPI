from src.application.read_model.manager import ManagerData

from ..collector import serialize_collector_to_json
from ..ticket import serialize_ticket_to_json

def serialize_manager_to_json(manager: ManagerData) -> dict:
    return {
        "id": manager.id,
        "uuid": manager.uuid,
        "username": manager.username,
        "password": manager.password,
        "collectors": list(map(serialize_collector_to_json, manager.collectors)),
        "tickets": list(map(serialize_ticket_to_json, manager.tickets))
    }