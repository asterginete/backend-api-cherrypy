# tests/test_file_api.py

import unittest
import cherrypy
from app.views import file_api
from app.models import FileUpload
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE_URL
import os

class TestFileAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cherrypy.tree.mount(file_api.FileAPI(), '/api/file')
        cherrypy.engine.start()

    @classmethod
    def tearDownClass(cls):
        cherrypy.engine.exit()

    def test_get_files(self):
        # Simulate a GET request to the /api/file endpoint
        response = cherrypy.request("/api/file")
        self.assertEqual(response.status, 200)
        files = response.json()
        self.assertIsInstance(files, list)

    def test_upload_file(self):
        # Simulate a POST request to the /api/file/upload endpoint
        file_path = "path_to_some_test_file.jpg"
        with open(file_path, 'rb') as f:
            response = cherrypy.request("/api/file/upload", method="POST", files={"file": f})
        self.assertEqual(response.status, 201)
        uploaded_file = response.json()
        self.assertEqual(uploaded_file["filename"], os.path.basename(file_path))

    # Similarly, you can add more tests for other endpoints in the file_api

if __name__ == "__main__":
    unittest.main()
