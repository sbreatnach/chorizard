import os

# OIDC config options as per mozilla_django_oidc.
# can get most of these from Keycloak at discovery endpoint:
# http://localhost:8080/realms/chorizard/.well-known/openid-configuration
OIDC_OP_JWKS_ENDPOINT = os.getenv(
    "OIDC_JWKS_ENDPOINT",
    "http://localhost:8080/realms/chorizard/protocol/openid-connect/certs",
)
OIDC_RP_CLIENT_ID = os.getenv("OIDC_CLIENT_ID", "account")
OIDC_RP_CLIENT_SECRET = os.getenv("OIDC_CLIENT_SECRET", "dummy")
OIDC_OP_AUTHORIZATION_ENDPOINT = os.getenv(
    "OIDC_AUTH_ENDPOINT",
    "http://localhost:8080/realms/chorizard/protocol/openid-connect/auth",
)
OIDC_OP_TOKEN_ENDPOINT = os.getenv(
    "OIDC_TOKEN_ENDPOINT",
    "http://localhost:8080/realms/chorizard/protocol/openid-connect/token",
)
OIDC_OP_USER_ENDPOINT = os.getenv(
    "OIDC_USER_ENDPOINT",
    "http://localhost:8080/realms/chorizard/protocol/openid-connect/userinfo",
)
OIDC_OP_LOGOUT_ENDPOINT = os.getenv(
    "OIDC_LOGOUT_ENDPOINT",
    "http://localhost:8080/realms/chorizard/protocol/openid-connect/logout",
)

OIDC_RP_SIGN_ALGO = "RS256"
OIDC_OP_LOGOUT_URL_METHOD = "chorizard.oidc.provider_logout_url"

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
