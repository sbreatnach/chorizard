"""
Django settings for chorizard project.

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv


def is_env_truthy(key, default=""):
    return os.getenv(key, default).lower() in {"true", "t", "1"}


load_dotenv(os.getenv("ENV_FILE", ".env"))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    "SECRET_KEY", "django-insecure-n)^s5o)^sfumqwziv0yzn84ph+re9(#z@&nehwla1pvyx63nqj"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = is_env_truthy("DEBUG", "true")

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "mozilla_django_oidc",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "mozilla_django_oidc.middleware.SessionRefresh",
]

AUTHENTICATION_BACKENDS = [
    "mozilla_django_oidc.auth.OIDCAuthenticationBackend",
]

ROOT_URLCONF = "chorizard.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "chorizard.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "chorizard",
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": int(os.getenv("DB_PORT", "5432")),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# OIDC config options as per mozilla_django_oidc.
# can get most of these from Keycloak at discovery endpoint:
# http://localhost:8080/realms/chorizard/.well-known/openid-configuration
OIDC_OP_JWKS_ENDPOINT = os.getenv(
    "OIDC_JWKS_ENDPOINT",
    "http://keycloak:8080/realms/chorizard/protocol/openid-connect/certs",
)
OIDC_RP_CLIENT_ID = os.getenv("OIDC_CLIENT_ID", "account")
OIDC_RP_CLIENT_SECRET = os.getenv(
    "OIDC_CLIENT_SECRET", "ZstDq0nBEwbjGNVcHWXizxEH3qOZio8X"
)
OIDC_OP_AUTHORIZATION_ENDPOINT = os.getenv(
    "OIDC_AUTH_ENDPOINT",
    "http://keycloak:8080/realms/chorizard/protocol/openid-connect/auth",
)
OIDC_OP_TOKEN_ENDPOINT = os.getenv(
    "OIDC_TOKEN_ENDPOINT",
    "http://keycloak:8080/realms/chorizard/protocol/openid-connect/token",
)
OIDC_OP_USER_ENDPOINT = os.getenv(
    "OIDC_USER_ENDPOINT",
    "http://localhost:8080/realms/chorizard/protocol/openid-connect/userinfo",
)

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
