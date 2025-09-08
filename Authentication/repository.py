from Repository.base_repository import BaseRepository
from Authentication.models import User
from Services.email_service import send_verification_email
import uuid

class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)
        
    
    def create_user_with_email(self, email, password=None, **extra_fields):

        user = User.objects.create_user(email=email, password=password, **extra_fields)
        user.email_verification_token = str(uuid.uuid4().hex[10]) + str(uuid.uuid4().hex[10])
        user.is_active = False
        user.is_verified = False
        user.save()

        email_sent = send_verification_email(user.email, user.email_verification_token)
        if not email_sent:
            # Since the user didn't verify the mail, we delete the user so that the original user can open an account with this email.
            
            user.delete()
            raise Exception("Could not send verification email. Please try again.")
        
        return user
