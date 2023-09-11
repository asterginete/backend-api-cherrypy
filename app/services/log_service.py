# app/services/log_service.py

from app.models import Log
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE_URL
from sqlalchemy import create_engine

# Setting up the database session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

class LogService:

    @staticmethod
    def log_event(user_id, level, message):
        """Log an event or action in the system."""
        session = Session()
        try:
            log_entry = Log(user_id=user_id, level=level, message=message)
            session.add(log_entry)
            session.commit()
        finally:
            session.close()

    @staticmethod
    def get_logs():
        """Retrieve all logs from the system."""
        session = Session()
        try:
            logs = session.query(Log).order_by(Log.timestamp.desc()).all()
            return logs
        finally:
            session.close()

    @staticmethod
    def get_log_by_id(log_id):
        """Retrieve a specific log by its ID."""
        session = Session()
        try:
            log = session.query(Log).filter_by(id=log_id).first()
            return log
        finally:
            session.close()

    @staticmethod
    def delete_log(log_id):
        """Delete a specific log by its ID."""
        session = Session()
        try:
            log = session.query(Log).filter_by(id=log_id).first()
            if log:
                session.delete(log)
                session.commit()
            else:
                raise ValueError("Log not found")
        finally:
            session.close()
