FROM mcr.microsoft.com/mssql/server:latest 

ENV ACCEPT_EULA Y 
ENV MSSQL_SA_PASSWORD devpassword12!

COPY ./create_dev_database.sql ./create_dev_database.sql
COPY ./create_database.sh ./create_database.sh

EXPOSE 1433

CMD ./create_database.sh & /opt/mssql/bin/sqlservr 
