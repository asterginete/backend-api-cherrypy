# config/logging_config.py

import os

LOGGING_DIR = os.path.join(os.getcwd(), 'logs')
if not os.path.exists(LOGGING_DIR):
    os.makedirs(LOGGING_DIR)

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGGING_DIR, 'app.log'),
            'formatter': 'standard'
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGGING_DIR, 'error.log'),
            'formatter': 'standard'
        }
    },
    'loggers': {
        '': {
            'handlers': ['default', 'error'],
            'level': 'DEBUG',
            'propagate': True
        }
    }
}
