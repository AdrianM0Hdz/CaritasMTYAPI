FROM ubuntu:18.04

WORKDIR /caritasapp

RUN apt-get update

# python 
RUN apt-get -y install software-properties-common
RUN apt-get -y install python3.7 
RUN apt-get -y install python3-venv
RUN apt-get -y install python3.7-venv
RUN apt-get -y install python3-pip

# microsoft odbc drivers

RUN apt-get -y install curl
RUN apt-get -y install apt-transport-https

COPY . ./

RUN bash ./install_odbc_driver.sh

EXPOSE 5000
EXPOSE 1434

RUN python3.7 -m venv env
RUN . ./env/bin/activate
RUN python3.7 -m pip install -U pip
RUN pip install -r requirements.txt

CMD ["python3.7", "app.py"]
