# tests/test_log_api.py

import unittest
import cherrypy
from app.views import log_api
from app.models import Log
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE_URL

class TestLogAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cherrypy.tree.mount(log_api.LogAPI(), '/api/log')
        cherrypy.engine.start()

    @classmethod
    def tearDownClass(cls):
        cherrypy.engine.exit()

    def test_get_logs(self):
        # Simulate a GET request to the /api/log endpoint
        response = cherrypy.request("/api/log")
        self.assertEqual(response.status, 200)
        logs = response.json()
        self.assertIsInstance(logs, list)

    def test_create_log(self):
        # Simulate a POST request to the /api/log endpoint
        data = {
            "message": "Test log message",
            "level": "INFO"
        }
        response = cherrypy.request("/api/log", method="POST", json=data)
        self.assertEqual(response.status, 201)
        log = response.json()
        self.assertEqual(log["message"], data["message"])
        self.assertEqual(log["level"], data["level"])

    # Similarly, you can add more tests for other endpoints in the log_api

if __name__ == "__main__":
    unittest.main()
