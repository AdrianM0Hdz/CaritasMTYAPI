import os 

import pyodbc

from src.application.read_model.ticket import TicketData, TicketState

from src.infrastructure.persistence.queries.serializers.ticket.deserialize_ticket import deserialize_ticket

def get_ticket_by_id(id: int) -> TicketData:
    connectionstring = f'DRIVER={{ODBC Driver 17 for SQL Server}}; \
                             SERVER={os.environ["SERVER"]}; \
                             DATABASE={os.environ["DATABASE"]}; \
                             UID={os.environ["USERNAME"]}; \
                             PWD={os.environ["PASSWORD"]}'  
    conn = pyodbc.connect(connectionstring)
    cursor = conn.cursor()

    query = f"SELECT * FROM Ticket WHERE ID='{id}'"
    cursor.execute(query)
    
    data = cursor.fetchall() 
    
    if len(data) != 1:
        raise BaseException("More than one item fetched")
     
    ticket_raw_data = data[0]

    return deserialize_ticket(ticket_raw_data)