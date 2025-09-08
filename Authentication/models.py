from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import User

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True.')

        return self.create_user(username, email, password, **extra_fields)
    

class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    email_varification_token = models.CharField(max_length=100, blank=True, null=True)
    is_acitive = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_social_user = models.BooleanField(default=False)
    date_of_birth = models.DateField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    mail_link_expires_at = models.DateTimeField(blank=True, null=True)
    
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    
    def __str__(self):
        return self.email

    def is_email_verification_expired(self):
        """Check if email verification has expired"""
        if not self.mail_link_expires_at or self.is_active:
            return False
        return timezone.now() > self.mail_link_expires_at

    
    def verify_email(self):
        self.is_active = True
        self.is_verified = True
        self.email_verification_token = None
        self.save()


    class Meta:
        ordering = ['id']
