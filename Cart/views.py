from django.shortcuts import render
from rest_framework import status
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .serializers import CartSerializer
from Cart.repository import CartRepository
from Custom_Permissions import custom_permissions

# Creating my views


class CartViewSet(ModelViewSet):
    queryset = CartRepository().get_all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_classe = CartSerializer
    
    
    