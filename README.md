# chorizard

# Install

```shell
export COMPOSE_VERSION=v2.20.3
curl -SL https://github.com/docker/compose/releases/download/${COMPOSE_VERSION}/docker-compose-linux-x86_64 -o docker-compose
sudo install docker-compose /usr/local/bin && rm docker-compose

poetry shell
poetry install
pre-commit install
```

All further commands assume you are running within a `poetry shell`.

# Local Testing Setup

```shell
docker-compose up
python manage.py migrate
python manage.py createsuperuser
```

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

## Running

```shell
python manage.py runserver
```

When creating an OIDC user in Keycloak, ensure that the user has an email that
has been marked as verified.
