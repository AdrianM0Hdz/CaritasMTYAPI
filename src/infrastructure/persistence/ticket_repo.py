import os

import pyodbc 

from src.utils import execute_command, execute_query

from src.domain.ticket import Ticket
from src.domain.ticket.ticket_state import TicketState

class TicketRepository:

    def insert(self, item: Ticket):    
        command=f""" INSERT INTO 
                     Ticket (ID, 
                             ManagerID, 
                             CollectorID, 
                             HousingReference, 
                             ReceiptComments, 
                             ReprogrammationComments, 
                             HousePhoneNumber, 
                             Cellphone, 
                             State, 
                             TicketDate, 
                             CollectorComments) 
                     VALUES ('{item.id}', 
                             '{item.manager_id}', 
                             '{item.collector_id}', 
                             '{item.housing_reference}', 
                             '{item.receipt_comments}',
                             '{item.reprogramation_comments}',
                             '{item.house_phone_number}', 
                             '{item.cellphone}',
                             '{item.state.value}',
                             '{str(item.date)}',
                             '{item.collector_comments}');"""
        execute_command(command)

    def get(self, id: str) -> Ticket:
        query = f"SELECT * FROM Ticket WHERE ID='{id}'"
        raw_data = execute_query(query)
        if len(raw_data) > 1:
            raise Exception("more than one item fetched")
        if len(raw_data) == 0:
            raise Exception("no ticket with that id found")
        item_row = raw_data[0]
        return Ticket(
            id=item_row[0],
            manager_id=item_row[1],
            collector_id=item_row[2],
            housing_reference=item_row[3],
            receipt_comments=item_row[4],
            reprogramation_comments=item_row[5],
            house_phone_number=item_row[6],
            cellphone=item_row[7],
            state=TicketState(item_row[8]),
            date=item_row[9],
            collector_comments=item_row[10]
        )

    def commit(self, item: Ticket):
        command = f"""UPDATE Ticket SET
                      ID='{item.id}', 
                      ManagerID='{item.manager_id}', 
                      CollectorID='{item.collector_id}', 
                      HousingReference='{item.housing_reference}', 
                      ReceiptComments='{item.receipt_comments}', 
                      ReprogrammationComments='{item.reprogramation_comments}', 
                      HousePhoneNumber='{item.house_phone_number}', 
                      Cellphone='{item.cellphone}', 
                      State='{item.state}', 
                      TicketDate='{item.date}', 
                      CollectorComments='{item.collector_comments}'
                      WHERE ID='{item.id}';"""
        execute_command(command)
