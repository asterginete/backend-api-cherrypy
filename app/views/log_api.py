# app/views/log_api.py

import cherrypy
from app.models import Log
from app.utils.auth import require, validate_password
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE_URL
from sqlalchemy import create_engine

# Setting up the database session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

class LogAPI:
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.auth_basic(realm='localhost', checkpassword=validate_password)
    @require('admin')  # Assuming only admin can view logs
    def index(self):
        session = Session()
        try:
            logs = session.query(Log).order_by(Log.timestamp.desc()).all()
            return [{"id": log.id, "user_id": log.user_id, "level": log.level, "message": log.message, "timestamp": str(log.timestamp)} for log in logs]
        finally:
            session.close()

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.auth_basic(realm='localhost', checkpassword=validate_password)
    @require('admin')  # Assuming only admin can view specific logs
    def get(self, log_id):
        session = Session()
        try:
            log = session.query(Log).filter_by(id=log_id).first()
            if log:
                return {
                    "id": log.id,
                    "user_id": log.user_id,
                    "level": log.level,
                    "message": log.message,
                    "timestamp": str(log.timestamp)
                }
            else:
                raise cherrypy.HTTPError(404, "Log not found")
        finally:
            session.close()
