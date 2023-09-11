# app/services/token_service.py

import jwt
from datetime import datetime, timedelta
from app.models import APIToken
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE_URL
from sqlalchemy import create_engine

# Setting up the database session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

SECRET_KEY = "YOUR_SECRET_KEY"  # This should be stored securely, not hardcoded

class TokenService:

    @staticmethod
    def generate_token(user_id):
        """Generate a JWT token for a user."""
        payload = {
            "user_id": user_id,
            "exp": datetime.utcnow() + timedelta(days=1)  # Token expires in 1 day
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        return token

    @staticmethod
    def validate_token(token):
        """Validate a JWT token."""
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            raise ValueError("Token has expired")
        except jwt.InvalidTokenError:
            raise ValueError("Invalid token")

    @staticmethod
    def store_token(user_id, token):
        """Store the token in the database."""
        session = Session()
        try:
            api_token = APIToken(user_id=user_id, token=token)
            session.add(api_token)
            session.commit()
        finally:
            session.close()

    @staticmethod
    def revoke_token(token):
        """Revoke a token by removing it from the database."""
        session = Session()
        try:
            api_token = session.query(APIToken).filter_by(token=token).first()
            if api_token:
                session.delete(api_token)
                session.commit()
            else:
                raise ValueError("Token not found in the database")
        finally:
            session.close()
