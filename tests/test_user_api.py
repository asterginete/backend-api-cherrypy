# tests/test_user_api.py

import unittest
import cherrypy
from app.views import user_api
from app.models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE_URL
import json

class TestUserAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cherrypy.tree.mount(user_api.UserAPI(), '/api/user')
        cherrypy.engine.start()

    @classmethod
    def tearDownClass(cls):
        cherrypy.engine.exit()

    def test_get_users(self):
        # Simulate a GET request to the /api/user endpoint
        response = cherrypy.request("/api/user")
        self.assertEqual(response.status, 200)
        users = json.loads(response.body.read())
        self.assertIsInstance(users, list)

    def test_get_user_by_id(self):
        # Simulate a GET request to the /api/user/{id} endpoint
        user_id = 1
        response = cherrypy.request(f"/api/user/{user_id}")
        self.assertEqual(response.status, 200)
        user_data = json.loads(response.body.read())
        self.assertEqual(user_data["id"], user_id)

    def test_create_user(self):
        # Simulate a POST request to the /api/user endpoint
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "newpassword"
        }
        response = cherrypy.request("/api/user", method="POST", json=data)
        self.assertEqual(response.status, 201)
        user_data = json.loads(response.body.read())
        self.assertEqual(user_data["username"], data["username"])

    # Similarly, you can add more tests for other endpoints in the user_api

if __name__ == "__main__":
    unittest.main()
