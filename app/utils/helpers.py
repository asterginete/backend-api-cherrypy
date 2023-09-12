# app/utils/helpers.py

import os
import hashlib
from datetime import datetime

def generate_file_path(filename, user_id):
    """
    Generate a unique file path for uploaded files.
    This can be used to avoid filename collisions.
    """
    # Generate a hash of the filename and current timestamp
    name, ext = os.path.splitext(filename)
    hash_name = hashlib.md5(f"{name}{datetime.now()}".encode()).hexdigest()
    return f"uploads/{user_id}/{hash_name}{ext}"

def hash_password(password):
    """
    Hash a password for storing in the database.
    This uses a simple MD5 hash for demonstration purposes.
    In a real-world scenario, you'd use a more secure hashing method.
    """
    return hashlib.md5(password.encode()).hexdigest()

def verify_password(stored_password, provided_password):
    """
    Verify a password against its hashed version.
    """
    return stored_password == hash_password(provided_password)

def format_datetime(value, format='%Y-%m-%d %H:%M:%S'):
    """
    Format a datetime object as a string.
    """
    return value.strftime(format)
