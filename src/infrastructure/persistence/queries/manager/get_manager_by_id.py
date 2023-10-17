import os 

import pyodbc

from src.application.read_model.manager import ManagerData
from src.utils.execute_query import execute_query

from src.infrastructure.persistence.queries.ticket.get_tickets_by_manager_id import get_tickets_by_manager_id
from src.infrastructure.persistence.queries.collector.get_collectors_by_manager_id import get_collectors_by_manager_id

from src.infrastructure.persistence.queries.serializers.manager.deserialize_manager import deserialize_manager

def get_manager_by_id(id: int) -> ManagerData:
    query = f"SELECT * FROM Manager WHERE ID=?"
    params = [id]
    
    data = execute_query(query, params)
    
    if len(data) == 0:
        raise BaseException("There's no manager with that ID")

    if len(data) > 1:
        raise BaseException("More than one item fetched, check IDs")
     
    manager_raw_data = data[0]
    managerID = manager_raw_data[0]

    tickets = get_tickets_by_manager_id(managerID)
    collectors = get_collectors_by_manager_id(managerID)

    return deserialize_manager(manager_raw_data, list(tickets), list(collectors))

