# app/models/user.py

from sqlalchemy import create_engine, Column, Integer, String, Sequence, ForeignKey, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    hashed_password = Column(String(128), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    profile = relationship("UserProfile", uselist=False, back_populates="user")
    tokens = relationship("APIToken", back_populates="user")
    uploads = relationship("FileUpload", back_populates="user")

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)


class UserProfile(Base):
    __tablename__ = 'user_profiles'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    first_name = Column(String(50))
    last_name = Column(String(50))
    avatar = Column(String(255))  # URL to the image, if using S3 or similar for storage
    bio = Column(String(500))

    user = relationship("User", back_populates="profile")


class APIToken(Base):
    __tablename__ = 'api_tokens'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    token = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, default=func.now())
    expires_at = Column(DateTime)

    user = relationship("User", back_populates="tokens")


class FileUpload(Base):
    __tablename__ = 'file_uploads'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    file_url = Column(String(255), nullable=False)  # URL to the file, if using S3 or similar for storage
    created_at = Column(DateTime, default=func.now())

    user = relationship("User", back_populates="uploads")
