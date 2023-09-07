import pyodbc
from pyodbc import Row
print(pyodbc.drivers())

SERVER = '10.14.255.68'
DATABASE = 'DB_INGRESOS'
USERNAME = 'SA'
PASSWORD = 'Shakira123.'

connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

conn = pyodbc.connect(connectionString)

query = """
    SELECT * FROM Manager;
"""

cursor = conn.cursor() 
cursor.execute(query)
for record in cursor.fetchall():
    print(record[0])

