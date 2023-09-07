import os 

import pyodbc

from src.application.read_model.manager import ManagerData

from src.infrastructure.persistence.queries.ticket.get_tickets_by_manager_id import get_tickets_by_manager_id
from src.infrastructure.persistence.queries.collector.get_collectors_by_manager_id import get_collectors_by_manager_id

from src.infrastructure.persistence.queries.serializers.manager.deserialize_manager import deserialize_manager

def get_manager_by_id(id: str) -> ManagerData:
    connectionstring = f'DRIVER={{ODBC Driver 17 for SQL Server}}; \
                             SERVER={os.environ["SERVER"]}; \
                             DATABASE={os.environ["DATABASE"]}; \
                             UID={os.environ["USERNAME"]}; \
                             PWD={os.environ["PASSWORD"]}'  
    conn = pyodbc.connect(connectionstring)
    cursor = conn.cursor()

    query = f"SELECT * FROM Manager WHERE ID='{id}'"
    cursor.execute(query)
    
    data = cursor.fetchall() 
    
    if len(data) == 0:
        raise BaseException("There's no manager with that ID")

    if len(data) > 1:
        raise BaseException("More than one item fetched, check IDs")
     
    manager_raw_data = data[0]
    managerID = manager_raw_data[0]

    tickets = get_tickets_by_manager_id(managerID)
    collectors = get_collectors_by_manager_id(managerID)

    return deserialize_manager(manager_raw_data, list(tickets), list(collectors))

