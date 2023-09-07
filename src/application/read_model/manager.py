from dataclasses import dataclass
from typing import List

from .collector import CollectorData
from .ticket import TicketData


@dataclass(frozen=True)
class ManagerData:
    id: str
    username: str
    password: str
    tickets: List[TicketData]
    collectors: List[CollectorData]
