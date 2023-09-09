# chorizard

# Install

```shell
poetry shell
poetry install
export COMPOSE_VERSION=v2.20.3
curl -SL https://github.com/docker/compose/releases/download/${COMPOSE_VERSION}/docker-compose-linux-x86_64 -o docker-compose
sudo install docker-compose /usr/local/bin && rm docker-compose

pre-commit install
```

All further commands assume you are running within a `poetry shell`.
