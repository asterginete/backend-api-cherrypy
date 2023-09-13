# User Management Backend System with CherryPy

A comprehensive backend system for user management, token generation, file uploads, logging, and email queuing.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features

1. **User Management**: Create, update, retrieve, and delete users.
2. **Token Generation**: Generate and validate JWT tokens for user authentication.
3. **File Upload**: Allow users to upload files and retrieve file metadata.
4. **Logging**: Log important system events and retrieve logs.
5. **Email Queue**: Queue emails to be sent out to users.
6. **Database Integration**: Uses PostgreSQL for data persistence.
7. **Asynchronous Tasks**: Uses Celery for handling asynchronous tasks like sending emails.
8. **Error Handling**: Comprehensive error handling and validation.
9. **Authentication & Authorization**: Secure endpoints with JWT authentication and role-based authorization.
10. **Logging**: Integrated logging system for tracking system events and errors.

... [other features as listed previously]

## Installation

### Prerequisites

- Python 3.8+
- PostgreSQL
- Redis (for Celery)

### Steps

1. Clone the repository:

```bash
git clone https://github.com/asterginete/backend-api-cherrypy.git
cd backend-api-cherrypy
```

2. Install dependencies using pipenv:

```bash
pipenv install
```

3. Set up environment variables. Copy the `.env.example` to `.env` and modify the values:

```bash
cp .env.example .env
```

4. Initialize the database:

```bash
python db/init_db.py
```

5. Start the application:

```bash
python run.py
```

## Usage

Once the application is running, you can access the API endpoints using tools like `curl` or Postman.

## API Endpoints

### User API

- **GET** `/api/user`: Retrieve all users.
- **GET** `/api/user/<id>`: Retrieve a user by ID.
- **POST** `/api/user`: Create a new user.
... [other endpoints]

### Token API

- **POST** `/api/token/generate`: Generate a JWT token for a user.
... [other endpoints]

... [other APIs]

## Testing

To run the tests:

```bash
python -m unittest discover tests
```

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request.

## License

This project is licensed under the MIT License.
