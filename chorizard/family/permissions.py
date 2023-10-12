import functools

from chorizard.permissions import as_reference as as_reference_base
from .models import User

__all__ = [
    "as_reference",
]

MODEL_REFERENCE_TYPES = {
    User: "user",
}

as_reference = functools.partial(as_reference_base, MODEL_REFERENCE_TYPES)
