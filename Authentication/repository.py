from Base_Repository.base_repository import BaseRepository
from Authentication.models import User
from Authentication.Services.email_service import send_verification_email
import uuid

class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)
    
    def create_user_with_email(self, email, password=None, **extra_fields):
        user = User.objects.create(email=email, password=password, **extra_fields)
        user.email_verification_token = str(uuid.uuid4().hex[10]) + str(uuid.uuid4().hex[10])
        user.is_active = False
        user.is_verified = False
        user.save()

    # Send email asynchronously
        send_verification_email.delay(user.email, user.email_verification_token)
        
        delete_unverified_user.apply_async(
                args=(user.id,), 
                eta=timezone.now() + timedelta(hours=12)
            )

        # Don't delete immediately; you can clean up later via a scheduled task
        return user
