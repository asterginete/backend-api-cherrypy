# app/models/log.py

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Log(Base):
    __tablename__ = 'logs'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)  # Nullable, as not all logs may be associated with a user
    level = Column(Enum('INFO', 'ERROR', 'WARNING', 'DEBUG', name='log_levels'), nullable=False)
    message = Column(String, nullable=False)
    timestamp = Column(DateTime, default=func.now())
