import os 

import pyodbc

from src.application.read_model.collector import CollectorData

from src.infrastructure.persistence.queries.ticket.get_tickets_by_collector_id import get_tickets_by_collector_id
from src.infrastructure.persistence.queries.serializers.collector.deserialize_collector import deserialize_collector

def get_collector_by_username(username: str) -> CollectorData:
    connectionstring = f'DRIVER={{ODBC Driver 17 for SQL Server}}; \
                             SERVER={os.environ["SERVER"]}; \
                             DATABASE={os.environ["DATABASE"]}; \
                             UID={os.environ["USERNAME"]}; \
                             PWD={os.environ["PASSWORD"]}'  
    conn = pyodbc.connect(connectionstring)
    cursor = conn.cursor()

    query = f"SELECT * FROM Collector WHERE username='{username}'"
    cursor.execute(query)
    
    data = cursor.fetchall() 
    
    if len(data) == 0:
        raise BaseException("NO COLLECTOR WITH THAT USERNAME FOUND")

    if len(data) > 1:
        raise BaseException("MORE THAN ONE COLLECTOR WITH THAT USERNAME")
     
    collector_raw_data = data[0]

    tickets = get_tickets_by_collector_id(collector_raw_data[0])

    return deserialize_collector(collector_raw_data, list(tickets))

