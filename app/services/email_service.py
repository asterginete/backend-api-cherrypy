# app/services/email_service.py

import smtplib
from email.message import EmailMessage
from config.settings import EMAIL_HOST, EMAIL_PORT, EMAIL_USE_TLS, EMAIL_USERNAME, EMAIL_PASSWORD

class EmailService:

    @staticmethod
    def send_email(subject, body, to_email):
        """Send an email."""
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = EMAIL_USERNAME
        msg['To'] = to_email

        try:
            with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
                if EMAIL_USE_TLS:
                    server.starttls()
                server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
                server.send_message(msg)
        except Exception as e:
            # In a real-world scenario, you'd probably log this exception and potentially raise a custom exception.
            print(f"Error sending email: {e}")

    @staticmethod
    def send_welcome_email(user_email, user_name):
        """Send a welcome email to a new user."""
        subject = "Welcome to Our Service!"
        body = f"Hello {user_name},\n\nThank you for registering with our service. We're glad to have you on board!"
        EmailService.send_email(subject, body, user_email)

    @staticmethod
    def send_password_reset_email(user_email, reset_link):
        """Send a password reset email."""
        subject = "Password Reset Request"
        body = f"We received a request to reset your password. Click the link below to reset it:\n\n{reset_link}\n\nIf you didn't request this, please ignore this email."
        EmailService.send_email(subject, body, user_email)
