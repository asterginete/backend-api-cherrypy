# app/services/file_service.py

from app.models import FileUpload, User
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE_URL
from sqlalchemy import create_engine

# Setting up the database session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

class FileService:

    @staticmethod
    def upload_file(user_id, file):
        """Upload a file and store its metadata in the database."""
        session = Session()
        try:
            # Logic to save the file and get the file_url
            # For now, we'll just simulate a file_url
            file_url = f"http://example.com/files/{file.filename}"

            new_file = FileUpload(user_id=user_id, file_url=file_url)
            session.add(new_file)
            session.commit()

            return new_file
        finally:
            session.close()

    @staticmethod
    def get_files(user_id=None):
        """Retrieve all files or files specific to a user."""
        session = Session()
        try:
            query = session.query(FileUpload)
            if user_id:
                query = query.filter_by(user_id=user_id)
            files = query.all()
            return files
        finally:
            session.close()

    @staticmethod
    def get_file_by_id(file_id):
        """Retrieve a specific file by its ID."""
        session = Session()
        try:
            file = session.query(FileUpload).filter_by(id=file_id).first()
            return file
        finally:
            session.close()

    @staticmethod
    def delete_file(file_id):
        """Delete a specific file and its metadata from the database."""
        session = Session()
        try:
            file = session.query(FileUpload).filter_by(id=file_id).first()
            if file:
                # Logic to delete the actual file from storage
                # For now, we'll just delete its metadata from the database
                session.delete(file)
                session.commit()
            else:
                raise ValueError("File not found")
        finally:
            session.close()
