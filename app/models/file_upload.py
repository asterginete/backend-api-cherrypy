# app/models/file_upload.py

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class FileUpload(Base):
    __tablename__ = 'file_uploads'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    file_url = Column(String(255), nullable=False)  # URL to the file, if using S3 or similar for storage
    created_at = Column(DateTime, default=func.now())

    user = relationship("User", back_populates="uploads")
