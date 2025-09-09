from django.shortcuts import render
from rest_framework import status
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer
from .repository import ProductRepository
from Custom_Permissions import custom_permissions

# Create your views here.

class ProductViewSet(ModelViewSet):
    queryset = ProductRepository().get_all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          custom_permissions.IsOwnerOrReadOnly]
    
    
