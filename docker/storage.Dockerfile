FROM postgres:16.0-alpine

COPY ./docker/entrypoint.sh /docker-entrypoint-initdb.d/initdb.sh
RUN chmod +x /docker-entrypoint-initdb.d/initdb.sh
