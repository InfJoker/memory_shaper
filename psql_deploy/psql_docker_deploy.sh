#!/bin/bash

docker run --name shpg -e POSTGRES_PASSWORD=p@ssw0rd -d -p 5432:5432 postgres
sleep 2

