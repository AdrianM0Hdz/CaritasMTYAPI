from hashlib import sha512

from src.application.read_model.manager import ManagerData
from src.infrastructure.persistence.queries.manager.get_manager_by_username import get_manager_by_username

def login_manager(username: str, password: str) -> ManagerData:
    manager: ManagerData = get_manager_by_username(username=username)
    hashed_password = sha512(bytes(password, "utf-8")).hexdigest()
    if manager.password != hashed_password:
        raise BaseException("INCORRECT PASSWORD")
    return manager
