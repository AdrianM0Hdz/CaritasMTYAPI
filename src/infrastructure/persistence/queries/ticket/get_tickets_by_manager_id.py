import os 
from typing import Tuple

import pyodbc

from src.application.read_model.ticket import TicketData
from src.utils.execute_query import execute_query

from src.infrastructure.persistence.queries.serializers.ticket.deserialize_ticket import deserialize_ticket

def get_tickets_by_manager_id(manager_id: int) -> Tuple[TicketData]:

    query = f"SELECT * FROM Ticket WHERE ManagerID=?"
    params = [manager_id]
    
    data = execute_query(query, params)
    
    tickets = tuple(map(deserialize_ticket, data))
    
    return tickets