from Authentication.task import send_mail_to_user

def send_verification_email(email, token):
    subject = "Verify your email"
    verification_link = f"http://localhost:8000/api/auth/verify-email/{token}/"
    message = f"Click the link to verify your account: {verification_link}"
    
    result = send_mail_to_user.delay(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        fail_silently=False,
    )
    return result