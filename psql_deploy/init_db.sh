#!/bin/bash

# фуууу костыль
apt-get update && apt-get install -y curl && apt-get clean

curl db:5432

# wait for db
while [[ $? != 52 ]];
  do curl db:5432;
done;

apt-get remove -y curl


psql -h db -p 5432 -U postgres -a -f psql_deploy/init.sql
