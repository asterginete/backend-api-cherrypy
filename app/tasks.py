# app/tasks.py

from celery import Celery
from app.services.email_service import EmailService
from app.models import EmailQueue
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE_URL, CELERY_BROKER_URL
from sqlalchemy import create_engine

# Setting up the database session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# Initialize Celery
celery_app = Celery('tasks', broker=CELERY_BROKER_URL)

@celery_app.task
def send_queued_emails():
    """
    Send emails from the email queue.
    """
    session = Session()
    try:
        emails = session.query(EmailQueue).filter_by(sent=False).all()
        for email in emails:
            EmailService.send_email(email.subject, email.body, email.to_email)
            email.sent = True
            session.commit()
    finally:
        session.close()

# Add more tasks as needed
