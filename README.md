## Note

Packaging instruction [here](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

## Build command

```sh
cd docker/dev
docker compose --env-file ../.env build --build-arg UID=$(id -u) --build-arg GID=$(id -g)
```

## Run command

```sh
docker compose --env-file ../../private.env --env-file ../.env up
```