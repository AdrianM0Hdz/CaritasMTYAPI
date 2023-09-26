import os 
from typing import Tuple

import pyodbc

from src.application.read_model.ticket import TicketData

from src.infrastructure.persistence.queries.serializers.ticket.deserialize_ticket import deserialize_ticket

def get_tickets_by_collector_id(collector_id: int) -> Tuple[TicketData, ...]:
    connectionstring = f'DRIVER={os.environ["SQL_SERVER_DRIVER"]}; \
                             SERVER={os.environ["SERVER"]}; \
                             DATABASE={os.environ["DATABASE"]}; \
                             UID={os.environ["USERNAME"]}; \
                             PWD={os.environ["PASSWORD"]}'  
    conn = pyodbc.connect(connectionstring)
    cursor = conn.cursor()

    query = f"SELECT * FROM Ticket WHERE CollectorID='{collector_id}'"
    cursor.execute(query)
    
    data = cursor.fetchall() 
    
    tickets = tuple(map(deserialize_ticket, data))
    
    return tickets