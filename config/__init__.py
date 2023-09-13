# config/__init__.py

from .settings import (
    DATABASE_URL, EMAIL_HOST, EMAIL_PORT, EMAIL_USE_TLS, EMAIL_USERNAME, EMAIL_PASSWORD,
    CELERY_BROKER_URL, JWT_SECRET, JWT_ALGORITHM, JWT_EXPIRATION_TIME,
    ALLOWED_FILE_EXTENSIONS, LOGGING_DIR
)

from .logging_config import LOGGING_CONFIG

# If you have any shared base classes, configurations, or initializations specific to config, you can define or import them here.
