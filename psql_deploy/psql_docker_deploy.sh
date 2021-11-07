#!/bin/bash

docker run --name shpg -e POSTGRES_PASSWORD=passw0rd -d -p 5432:5432 postgres

