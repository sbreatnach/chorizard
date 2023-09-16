import os
from dotenv import load_dotenv
from pathlib import Path

__all__ = [
    "is_env_truthy",
    "BASE_DIR",
]


def is_env_truthy(key, default=""):
    return os.getenv(key, default).lower() in {"true", "t", "1"}


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(os.getenv("ENV_FILE", ".env"))
