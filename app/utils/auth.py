# app/utils/auth.py

import cherrypy
from app.services.token_service import TokenService
from app.models import User
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE_URL
from sqlalchemy import create_engine

# Setting up the database session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def authenticate():
    """
    Authenticate the user based on the provided token.
    """
    token = cherrypy.request.headers.get('Authorization')
    if not token:
        raise cherrypy.HTTPError(401, "Authentication token is missing")

    try:
        payload = TokenService.validate_token(token)
        user_id = payload.get('user_id')
        session = Session()
        user = session.query(User).filter_by(id=user_id).first()
        if not user:
            raise cherrypy.HTTPError(401, "User not found")
        cherrypy.request.user = user
    except ValueError:
        raise cherrypy.HTTPError(401, "Invalid token")

def require(role):
    """
    Ensure the user has the required role.
    """
    def decorator(f):
        def wrapper(*args, **kwargs):
            user = cherrypy.request.user
            if not user or user.role != role:
                raise cherrypy.HTTPError(403, "You are not authorized to access this resource.")
            return f(*args, **kwargs)
        return wrapper
    return decorator
