import os 

import pyodbc

from src.application.read_model.ticket import TicketData, TicketState
from src.utils.execute_query import execute_query

from src.infrastructure.persistence.queries.serializers.ticket.deserialize_ticket import deserialize_ticket

def get_ticket_by_id(id: int) -> TicketData:
    query = f"SELECT * FROM Ticket WHERE ID=?"
    params = [id]
    
    data = execute_query(query, params)
    
    if len(data) != 1:
        raise BaseException("More than one item fetched")
     
    ticket_raw_data = data[0]

    return deserialize_ticket(ticket_raw_data)