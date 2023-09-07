import os 

import pyodbc

def execute_query(query: str) :

    connectionstring = f'DRIVER={{ODBC Driver 17 for SQL Server}}; \
                                SERVER={os.environ["SERVER"]}; \
                                DATABASE={os.environ["DATABASE"]}; \
                                UID={os.environ["USERNAME"]}; \
                                PWD={os.environ["PASSWORD"]}' 
     
    conn = pyodbc.connect(connectionstring)
    cursor = conn.cursor()
    cursor.execute(query)

    data = cursor.fetchall() 
    return data

