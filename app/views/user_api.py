# app/views/user_api.py

import cherrypy
from app.models import User, UserProfile
from app.utils.auth import require, validate_password
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE_URL
from sqlalchemy import create_engine
from app.utils.validators import validate_user_data

# Setting up the database session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

class UserAPI:
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.auth_basic(realm='localhost', checkpassword=validate_password)
    def index(self):
        session = Session()
        try:
            users = session.query(User).all()
            return [{"id": user.id, "username": user.username, "email": user.email} for user in users]
        finally:
            session.close()

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.auth_basic(realm='localhost', checkpassword=validate_password)
    def get(self, user_id):
        session = Session()
        try:
            user = session.query(User).filter_by(id=user_id).first()
            if user:
                return {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email
                }
            else:
                raise cherrypy.HTTPError(404, "User not found")
        finally:
            session.close()

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.auth_basic(realm='localhost', checkpassword=validate_password)
    def create(self, username, email, password):
        session = Session()
        try:
            # Data validation
            if not validate_user_data(username, email, password):
                raise cherrypy.HTTPError(400, "Invalid user data")

            new_user = User(username=username, email=email, password=password)  # Assuming password is hashed in the model
            session.add(new_user)
            session.commit()

            return {
                "id": new_user.id,
                "username": new_user.username,
                "email": new_user.email
            }
        finally:
            session.close()

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.auth_basic(realm='localhost', checkpassword=validate_password)
    def update(self, user_id, username=None, email=None, password=None):
        session = Session()
        try:
            user = session.query(User).filter_by(id=user_id).first()
            if not user:
                raise cherrypy.HTTPError(404, "User not found")

            if username:
                user.username = username
            if email:
                user.email = email
            if password:
                user.password = password  # Assuming password is hashed in the model

            session.commit()

            return {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
        finally:
            session.close()

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.auth_basic(realm='localhost', checkpassword=validate_password)
    def delete(self, user_id):
        session = Session()
        try:
            user = session.query(User).filter_by(id=user_id).first()
            if not user:
                raise cherrypy.HTTPError(404, "User not found")

            session.delete(user)
            session.commit()

            return {
                "message": "User deleted successfully"
            }
        finally:
            session.close()
