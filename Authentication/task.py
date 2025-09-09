from celery import shared_task
from django.utils import timezone
from .models import User

@shared_task
def cleanup_expired_users():
    """
    This task runs automatically based on schedule
    Deletes users whose email verification has expired
    """
    now = timezone.now()
    expired_users = User.objects.filter(
        is_active=False,
        email_expires_at__lt=now
    )
    
    count = expired_users.count()
    expired_users.delete()
    
    return f"Deleted {count} expired users at {now}"


@shared_task(bind=True, max_retries=3)
def send_mail_to_user(self, subject, message, from_email, recipient_list, fail_silently=False):
    try:
        return send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=fail_silently
        )
    except Exception as exc:
        # Retry up to 3 times with exponential backoff
        raise self.retry(exc=exc, countdown=5)
    
@shared_task
def delete_unverified_users():
    twelve_hours_ago = timezone.now() - timedelta(hours=12)
    unverified_users = User.objects.filter(
        is_verified=False,
        is_active=False,
        date_joined__lte=twelve_hours_ago
    )
    count = unverified_users.count()
    unverified_users.delete()
    return f"Deleted {count} unverified users"
