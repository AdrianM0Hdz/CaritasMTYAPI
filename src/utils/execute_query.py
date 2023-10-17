import os 

import pyodbc

def execute_query(query: str, params) :

    connectionstring = f'DRIVER={os.environ["SQL_SERVER_DRIVER"]}; \
                                SERVER={os.environ["SERVER"]}; \
                                DATABASE={os.environ["DATABASE"]}; \
                                UID={os.environ["USERNAME"]}; \
                                PWD={os.environ["PASSWORD"]}' 
     
    conn = pyodbc.connect(connectionstring)
    cursor = conn.cursor()
    cursor.execute(query, params)

    data = cursor.fetchall() 
    return data

