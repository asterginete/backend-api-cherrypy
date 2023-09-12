# app/utils/validators.py

import re

def validate_email(email):
    """
    Validate an email address.
    """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def validate_password(password):
    """
    Validate a password.
    For simplicity, we're checking if the password length is at least 8 characters.
    In a real-world scenario, you'd have more complex criteria.
    """
    return len(password) >= 8

def validate_username(username):
    """
    Validate a username.
    For simplicity, we're checking if the username length is between 3 and 20 characters.
    """
    return 3 <= len(username) <= 20

def validate_user_data(username, email, password):
    """
    Validate user registration data.
    """
    return validate_email(email) and validate_password(password) and validate_username(username)

def validate_file_extension(filename, allowed_extensions):
    """
    Validate the file extension of an uploaded file.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions
