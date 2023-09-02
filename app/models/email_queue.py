# app/models/email_queue.py

from sqlalchemy import Column, Integer, String, Enum, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EmailQueue(Base):
    __tablename__ = 'email_queue'
    
    id = Column(Integer, primary_key=True)
    recipient = Column(String(100), nullable=False)
    subject = Column(String(255), nullable=False)
    body = Column(String, nullable=False)
    status = Column(Enum('Pending', 'Sent', 'Failed', name='email_status'), default='Pending')
    created_at = Column(DateTime, default=func.now())
    sent_at = Column(DateTime)
