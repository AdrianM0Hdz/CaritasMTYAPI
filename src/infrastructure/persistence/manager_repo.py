"""
import pyodbc

print(pyodbc.drivers())

SERVER = '10.14.255.68'
DATABASE = 'DB_INGRESOS'
USERNAME = 'SA'
PASSWORD = 'Shakira123.'

connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

conn = pyodbc.connect(connectionString)

query =     SELECT * FROM Manager;

cursor = conn.cursor() 
cursor.execute(query)
for record in cursor.fetchall():
    print(record)


"""
import os

import pyodbc 

from src.domain.manager import Manager 
from src.domain.collector import Collector 
from src.domain.ticket import Ticket

class ManagerRepository:
    def __init__(self):     
        connectionstring = f'DRIVER={{ODBC Driver 17 for SQL Server}}; \
                             SERVER={os.environ["SERVER"]}; \
                             DATABASE={os.environ["DATABASE"]}; \
                             UID={os.environ["USERNAME"]}; \
                             PWD={os.environ["PASSWORD"]}'

        self.connection = pyodbc.connect(connectionstring)
    
    def insert(self, item: Manager):
        cursor = self.connection.cursor()
        
        query = f""" INSERT INTO Manager(UUID, Username, Password, Fullname) 
                     VALUES ('{item.uuid}', '{item.username}', '{item.password}', '{item.fullname}');"""
        
        cursor.execute(query)
        self.connection.commit()
        cursor.close()

    def commit(self, item: Manager):
        ...