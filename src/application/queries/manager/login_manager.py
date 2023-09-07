from hashlib import sha512

from src.application.read_model.manager import ManagerData
from src.infrastructure.persistence.queries.manager.get_manager_by_username import get_manager_by_username

def login_collector(username: str, password: str) -> CollectorData:
    collector: CollectorData = get_collector_by_username(username=username)
    hashed_password = sha512(bytes(password, "utf-8")).hexdigest()
    if collector.password != hashed_password:
        raise BaseException("INCORRECT PASSWORD")
    return collector

def login_manager(username: str, password: str) -> ManagerData:
    ...