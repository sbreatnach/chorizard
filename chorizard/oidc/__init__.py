from django.conf import settings
from urllib.parse import quote_plus


def provider_logout_url(request):
    redirect_uri = request.build_absolute_uri("/")
    return (
        f"{settings.OIDC_OP_LOGOUT_ENDPOINT}?"
        f"post_logout_redirect_uri={quote_plus(redirect_uri)}&"
        f"client_id={settings.OIDC_RP_CLIENT_ID}"
    )
