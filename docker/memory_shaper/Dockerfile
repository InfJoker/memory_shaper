FROM ubuntu:18.04

RUN apt-get update && apt-get install -y postgresql-client python-pip libpq-dev  && apt-get clean


COPY requirements.txt /
RUN pip install -r /requirements.txt
