from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from Profile.serializers import ProfileSerializer
from Profile.repository import ProfileRepository


# Create your views here.

class ProfileViewSet(ModelViewSet):
    queryset = ProfileRepository().get_all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    
