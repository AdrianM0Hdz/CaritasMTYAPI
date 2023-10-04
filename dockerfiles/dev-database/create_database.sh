#!/usr/bin/env bash

# wait for server to startup
sleep 30 

./opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P devpassword12! -i ./create_dev_database.sql