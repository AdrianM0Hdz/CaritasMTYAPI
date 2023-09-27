import os 
from typing import Tuple, List

import pyodbc

from src.application.read_model.collector import CollectorData
from src.utils.execute_query import execute_query
from src.infrastructure.persistence.queries.collector.get_collector_by_id import get_collector_by_id 

def get_collectors_by_manager_id(manager_id: int) -> Tuple[CollectorData, ...]:
    query = f"SELECT ID FROM Collector WHERE ManagerID='{manager_id}'"
    data = execute_query(query)
    ids: List[str] = list(map(lambda item: str(item[0]), data))
    collectors = tuple(map(get_collector_by_id, ids))
    return collectors