# config/settings.py

import os

# Database configurations
DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://username:password@localhost:5432/mydatabase')

# Email configurations
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.example.com')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587))
EMAIL_USE_TLS = bool(os.environ.get('EMAIL_USE_TLS', True))
EMAIL_USERNAME = os.environ.get('EMAIL_USERNAME', 'your_email@example.com')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD', 'your_email_password')

# Celery configurations
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/0')

# JWT configurations
JWT_SECRET = os.environ.get('JWT_SECRET', 'your_secret_key')
JWT_ALGORITHM = os.environ.get('JWT_ALGORITHM', 'HS256')
JWT_EXPIRATION_TIME = int(os.environ.get('JWT_EXPIRATION_TIME', 3600))  # 1 hour

# File upload configurations
ALLOWED_FILE_EXTENSIONS = set(os.environ.get('ALLOWED_FILE_EXTENSIONS', 'jpg,jpeg,png,gif').split(','))

# Logging directory
LOGGING_DIR = os.path.join(os.getcwd(), 'logs')

# Other configurations can be added as needed
