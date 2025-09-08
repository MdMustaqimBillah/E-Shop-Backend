from django.core.mail import send_mail
from django.conf import settings

def send_verification_email(email, token):
    subject = "Verify your email"
    verification_link = f"http://localhost:8000/api/auth/verify-email/{token}/"
    message = f"Click the link to verify your account: {verification_link}"
    
    sent = send_mail_to_user.delay(
        subject=subject,
        message=message,
        settings=settings.DEFAULT_FROM_EMAIL,
        email=[email],
        fail_silently=False,
    )
    return sent > 0  # True if at least 1 email was sent