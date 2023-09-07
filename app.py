import os
from dotenv import load_dotenv
load_dotenv(override=True)

from src.infrastructure.persistence.manager_repo import ManagerRepository
from src.domain.manager import Manager

from src.infrastructure.persistence.queries.ticket import get_ticket_by_id
from src.infrastructure.persistence.queries.ticket.get_tickets_by_collector_id import get_tickets_by_collector_id
from src.infrastructure.persistence.queries.collector.get_collector_by_id import get_collector_by_id
from src.infrastructure.persistence.queries.collector.get_collector_by_username import get_collector_by_username
from src.infrastructure.persistence.queries.collector.get_collectors_by_manager_id import get_collectors_by_manager_id

print(get_collectors_by_manager_id(manager_id="1"))