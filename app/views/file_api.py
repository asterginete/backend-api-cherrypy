# app/views/file_api.py

import cherrypy
from app.models import FileUpload, User
from app.utils.auth import require, validate_password
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE_URL
from sqlalchemy import create_engine

# Setting up the database session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

class FileAPI:
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.auth_basic(realm='localhost', checkpassword=validate_password)
    def index(self, user_id=None):
        session = Session()
        try:
            query = session.query(FileUpload)
            if user_id:
                query = query.filter_by(user_id=user_id)
            files = query.all()
            return [{"id": file.id, "user_id": file.user_id, "file_url": file.file_url, "created_at": str(file.created_at)} for file in files]
        finally:
            session.close()

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.auth_basic(realm='localhost', checkpassword=validate_password)
    def get(self, file_id):
        session = Session()
        try:
            file = session.query(FileUpload).filter_by(id=file_id).first()
            if file:
                return {
                    "id": file.id,
                    "user_id": file.user_id,
                    "file_url": file.file_url,
                    "created_at": str(file.created_at)
                }
            else:
                raise cherrypy.HTTPError(404, "File not found")
        finally:
            session.close()

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.auth_basic(realm='localhost', checkpassword=validate_password)
    def upload(self, user_id, file):
        # This is a simplified upload method. In a real-world scenario, you'd integrate with a service like S3.
        session = Session()
        try:
            user = session.query(User).filter_by(id=user_id).first()
            if not user:
                raise cherrypy.HTTPError(400, "User not found")

            # Logic to save the file and get the file_url
            # For now, we'll just simulate a file_url
            file_url = f"http://example.com/files/{file.filename}"

            new_file = FileUpload(user_id=user_id, file_url=file_url)
            session.add(new_file)
            session.commit()

            return {
                "id": new_file.id,
                "user_id": new_file.user_id,
                "file_url": new_file.file_url,
                "created_at": str(new_file.created_at)
            }
        finally:
            session.close()
