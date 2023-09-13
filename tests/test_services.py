# tests/test_services.py

import unittest
from app.services import TokenService, LogService, FileService, EmailService
from app.models import User, Token, Log, FileUpload, EmailQueue
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE_URL

class TestTokenService(unittest.TestCase):

    def test_generate_token(self):
        user = User(id=1, username="testuser", email="test@example.com")
        token = TokenService.generate_token(user)
        self.assertIsNotNone(token)

    def test_validate_token(self):
        user = User(id=1, username="testuser", email="test@example.com")
        token = TokenService.generate_token(user)
        payload = TokenService.validate_token(token)
        self.assertEqual(payload['user_id'], 1)

# Similarly, you can add tests for LogService, FileService, and EmailService

class TestLogService(unittest.TestCase):

    # Your LogService tests here

    pass

class TestFileService(unittest.TestCase):

    # Your FileService tests here

    pass

class TestEmailService(unittest.TestCase):

    # Your EmailService tests here

    pass

if __name__ == "__main__":
    unittest.main()
