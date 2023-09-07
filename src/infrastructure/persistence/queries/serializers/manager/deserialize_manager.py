from typing import List

from pyodbc import Row 

from src.application.read_model.manager import ManagerData
from src.application.read_model.collector import CollectorData
from src.application.read_model.ticket import TicketData

def deserialize_manager(manager_raw_data, tickets: List[TicketData], collectors: List[CollectorData]) -> ManagerData:
    return ManagerData(
        id=manager_raw_data[0],
        username=manager_raw_data[1],
        password=manager_raw_data[2],
        fullname=manager_raw_data[3],
        tickets=tickets,
        collectors=collectors
    )