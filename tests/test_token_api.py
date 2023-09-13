# tests/test_token_api.py

import unittest
import cherrypy
from app.views import token_api
from app.models import Token, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE_URL
import json

class TestTokenAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cherrypy.tree.mount(token_api.TokenAPI(), '/api/token')
        cherrypy.engine.start()

    @classmethod
    def tearDownClass(cls):
        cherrypy.engine.exit()

    def test_generate_token(self):
        # Simulate a POST request to the /api/token/generate endpoint
        data = {
            "username": "testuser",
            "password": "testpassword"
        }
        response = cherrypy.request("/api/token/generate", method="POST", json=data)
        self.assertEqual(response.status, 200)
        token_data = json.loads(response.body.read())
        self.assertIn("token", token_data)

    def test_validate_token(self):
        # First, generate a token
        data = {
            "username": "testuser",
            "password": "testpassword"
        }
        response = cherrypy.request("/api/token/generate", method="POST", json=data)
        token_data = json.loads(response.body.read())
        token = token_data["token"]

        # Now, validate the token
        response = cherrypy.request(f"/api/token/validate?token={token}")
        self.assertEqual(response.status, 200)
        validation_data = json.loads(response.body.read())
        self.assertEqual(validation_data["user_id"], 1)

    # Similarly, you can add more tests for other endpoints in the token_api

if __name__ == "__main__":
    unittest.main()
