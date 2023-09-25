import os 

import pyodbc

def execute_command(query: str) :
    connectionstring = f'DRIVER={os.environ["SQL_SERVER_DRIVER"]}; \
                                SERVER={os.environ["SERVER"]}; \
                                DATABASE={os.environ["DATABASE"]}; \
                                UID={os.environ["USERNAME"]}; \
                                PWD={os.environ["PASSWORD"]}' 
     
    conn = pyodbc.connect(connectionstring)
    cursor = conn.cursor()
    cursor.execute(query)

    conn.commit()
    return