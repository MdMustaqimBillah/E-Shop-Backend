from rest_framework import serializers
from .models import User
from Authentication.repository import UserRepository



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'date_of_birth', 'password', 'password2',]
        read_only_fields = [
            'id', 'date_joined', 'is_staff', 'is_superuser', 'is_acitive', 'is_verified', 'is_social_user', 'email_verification_token'
        ]

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        
        if  data['password'] and len(data['password']) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2', None)  # Removed password2 since it is not a field of user model

        email = validated_data.pop('email')
        password = validated_data.pop('password')

        user = UserRepository().create_user_with_email(
            email= email,
            password= password,
            **validated_data
        )

        if  not user:
            raise serializers.ValidationError("User could not be created. Please try again.")
        return user