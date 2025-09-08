from django.core.mail import send_mail
from django.conf import settings

def send_verification_email(email, token):
    subject = "Verify your email"
    verification_link = f"http://localhost:8000/api/verify-email/{token}/"
    message = f"Click the link to verify your account: {verification_link}"
    
    sent = send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )
    return sent > 0  # True if at least 1 email was sent