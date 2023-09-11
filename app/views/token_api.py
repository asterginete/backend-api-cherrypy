# app/views/token_api.py

import cherrypy
from app.models import APIToken, User
from app.utils.auth import require, validate_password
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE_URL
from sqlalchemy import create_engine
import jwt
from datetime import datetime, timedelta

# Setting up the database session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

SECRET_KEY = "YOUR_SECRET_KEY"  # This should be stored securely, not hardcoded

class TokenAPI:
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.auth_basic(realm='localhost', checkpassword=validate_password)
    def generate(self, user_id):
        session = Session()
        try:
            user = session.query(User).filter_by(id=user_id).first()
            if not user:
                raise cherrypy.HTTPError(400, "User not found")

            # Generate JWT token
            payload = {
                "user_id": user.id,
                "exp": datetime.utcnow() + timedelta(days=1)  # Token expires in 1 day
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

            # Store the token in the database
            api_token = APIToken(user_id=user.id, token=token)
            session.add(api_token)
            session.commit()

            return {
                "user_id": user.id,
                "token": token
            }
        finally:
            session.close()

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.auth_basic(realm='localhost', checkpassword=validate_password)
    @require('admin')  # Assuming only admin can revoke tokens
    def revoke(self, token):
        session = Session()
        try:
            api_token = session.query(APIToken).filter_by(token=token).first()
            if not api_token:
                raise cherrypy.HTTPError(400, "Token not found")

            session.delete(api_token)
            session.commit()

            return {
                "message": "Token revoked successfully"
            }
        finally:
            session.close()
