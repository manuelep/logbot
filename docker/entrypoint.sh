#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "postgres" <<-EOSQL
    CREATE USER ${DBUSERNAME} WITH PASSWORD '${DBUSERPASSWORD}';
	CREATE DATABASE ${DBNAME};
    GRANT ALL PRIVILEGES ON DATABASE ${DBNAME} TO ${DBUSERNAME};
EOSQL

psql -v ON_ERROR_STOP=1 --username "postgres" -d ${DBNAME} <<-EOSQL
    GRANT ALL PRIVILEGES ON SCHEMA public TO ${DBUSERNAME};
EOSQL