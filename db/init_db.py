# db/init_db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE_URL
from app.models import Base, User, Token, EmailQueue, FileUpload, Log

def init_database():
    """
    Initialize the database, create tables, and set up any initial data.
    """
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add any initial data if necessary
    # For example, you can create an admin user:
    # admin = User(username="admin", email="admin@example.com", password="hashed_password", role="admin")
    # session.add(admin)
    # session.commit()

    session.close()

if __name__ == "__main__":
    init_database()
