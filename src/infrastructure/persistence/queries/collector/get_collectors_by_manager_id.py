import os 
from typing import Tuple, List

import pyodbc

from src.application.read_model.collector import CollectorData

from src.infrastructure.persistence.queries.collector.get_collector_by_id import get_collector_by_id 

def get_collectors_by_manager_id(manager_id: int) -> Tuple[CollectorData, ...]:
    connectionstring = f'DRIVER={os.environ["SQL_SERVER_DRIVER"]}; \
                             SERVER={os.environ["SERVER"]}; \
                             DATABASE={os.environ["DATABASE"]}; \
                             UID={os.environ["USERNAME"]}; \
                             PWD={os.environ["PASSWORD"]}'  
    conn = pyodbc.connect(connectionstring)
    cursor = conn.cursor()

    query = f"SELECT ID FROM Collector WHERE ManagerID='{manager_id}'"
    cursor.execute(query)
    
    data = cursor.fetchall() 
    ids: List[str] = list(map(lambda item: str(item[0]), data))

    collectors = tuple(map(get_collector_by_id, ids))
    
    return collectors