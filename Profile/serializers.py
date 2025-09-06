from Profile.models import Profile
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']