import os
from dotenv import load_dotenv
load_dotenv(override=True)

from src.infrastructure.create_app import create_app

import pyodbc 
print(pyodbc.drivers())

app = create_app()

# TODO: this is provitional and for development
app.run(host="0.0.0.0", debug=True)
