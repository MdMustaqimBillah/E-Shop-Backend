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