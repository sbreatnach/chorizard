# chorizard

# Install

Assuming that the environment is an up-to-date Debian Linux OS, the following
steps will work (tested on Debian Bookworm).

```shell
# Python installed with poetry support
sudo apt install python-poetry

# docker-compose v2
export COMPOSE_VERSION=v2.20.3
curl -SL https://github.com/docker/compose/releases/download/${COMPOSE_VERSION}/docker-compose-linux-x86_64 -o docker-compose
sudo install docker-compose /usr/local/bin && rm docker-compose

# zed for permissions tests (https://github.com/authzed/zed)
sudo apt update && sudo apt install -y curl ca-certificates gpg
curl https://apt.fury.io/authzed/gpg.key | sudo apt-key add -
echo "deb https://apt.fury.io/authzed/ * *" > /etc/apt/sources.list.d/fury.list
sudo apt update && sudo apt install -y zed

poetry shell
poetry install
pre-commit install
```

All further commands assume you are running within a `poetry shell`.

# Local Testing Setup

## Services

```shell
# run all supporting services for the system
docker-compose up
# initialise the main Django DB
python manage.py migrate
python manage.py createsuperuser
```

## OIDC Configuration

Create a dedicated realm in [Keycloak](http://localhost:8080)
Create a `.env` file with the following:

```
OIDC_CLIENT_SECRET=dummy
```

Modify the auto-generated account client to
* Client authentication is ON
* Add `http://127.0.0.1:8000/*` to the valid redirect URIs
* Copy and paste the client key from the Credentials tab and set that as the
  value of OIDC_CLIENT_SECRET in `.env`

## Authz

Install the schema for system permissions:

```shell
zed schema write chorizard/permissions/permissions.zed
```

## Running

```shell
python manage.py runserver
```

When creating an OIDC user in Keycloak, ensure that the user has an email that
has been marked as verified.
