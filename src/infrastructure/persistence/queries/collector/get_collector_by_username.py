import os 

import pyodbc

from src.application.read_model.collector import CollectorData
from src.utils.execute_query import execute_query

from src.infrastructure.persistence.queries.ticket.get_tickets_by_collector_id import get_tickets_by_collector_id
from src.infrastructure.persistence.queries.serializers.collector.deserialize_collector import deserialize_collector

def get_collector_by_username(username: str) -> CollectorData:
    query = f"SELECT * FROM Collector WHERE username=?"
    params = [username]
    data = execute_query(query, params)
    
    if len(data) == 0:
        raise BaseException("NO COLLECTOR WITH THAT USERNAME FOUND")

    if len(data) > 1:
        raise BaseException("MORE THAN ONE COLLECTOR WITH THAT USERNAME")
     
    collector_raw_data = data[0]

    tickets = get_tickets_by_collector_id(collector_raw_data[0])

    return deserialize_collector(collector_raw_data, list(tickets))

