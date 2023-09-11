```
backend-api-cherrypy
│
├── app/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── token.py
│   │   ├── email_queue.py
│   │   ├── file_upload.py
│   │   └── log.py
│   │
│   ├── views/
│   │   ├── __init__.py
│   │   ├── user_api.py
│   │   ├── token_api.py       # Endpoints related to token management
│   │   ├── file_api.py        # Endpoints related to file uploads
│   │   └── log_api.py         # Endpoints for viewing logs (admin only)
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── email_service.py
│   │   ├── file_service.py
│   │   ├── log_service.py     # Service for logging actions/events
│   │   └── token_service.py   # Service for token generation and validation
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── validators.py
│   │   ├── error_handlers.py  # Utility functions for handling errors
│   │   └── helpers.py         # General helper functions
│   │
│   ├── __init__.py
│   └── tasks.py
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   └── logging_config.py
│
├── db/
│   ├── migrations/  # Database migration scripts (using Alembic)
│   └── init_db.py
│
├── tests/
│   ├── __init__.py
│   ├── test_user_api.py
│   ├── test_token_api.py      # Tests for token management
│   ├── test_file_api.py       # Tests for file uploads
│   ├── test_log_api.py        # Tests for log viewing
│   └── test_services.py       # Tests for various services
│
├── static/
│
├── templates/
│
├── .gitignore
├── README.md
└── run.py

```