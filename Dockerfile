FROM ubuntu:18.04

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y build-essential python3 python3-pip mysql-server

COPY src/ app/
WORKDIR app/

RUN pip3 install -r requirements.txt
RUN chmod +x server.py

EXPOSE 5000

CMD ./server.py
