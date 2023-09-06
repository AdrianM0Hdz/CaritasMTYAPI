import os
from dotenv import load_dotenv
load_dotenv(override=True)

from src.infrastructure.persistence.manager_repo import ManagerRepository
from src.domain.manager import Manager

m = Manager.create_new("manager_username_api", "manager_password_api", "manager_fullname_api")
r = ManagerRepository()

r.insert(m)