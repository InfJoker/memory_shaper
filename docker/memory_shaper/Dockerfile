FROM ubuntu:18.04

RUN apt-get update && apt-get install -y postgresql-client python3-pip libpq-dev  && apt-get clean


COPY requirements.txt /
RUN python3 -m pip install -r /requirements.txt
