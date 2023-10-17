import os

import pyodbc 

from src.domain.manager import Manager 
from src.domain.collector import Collector 
from src.domain.ticket import Ticket
from src.utils.execute_command import execute_command

class ManagerRepository:
    def __init__(self):     
        ...

    def insert(self, item: Manager):
        cursor = self.connection.cursor()
        
        query = f""" INSERT INTO Manager(UUID, Username, Password, Fullname) 
                     VALUES (?, ?, ?, ?);"""
        params = [item.uuid, item.username, item.password, item.fullname]

        execute_command(query, params)

    def commit(self, item: Manager):
        ...