from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Cart.views import CartViewSet

router = DefaultRouter()

router.register(r'cart', CartViewSet, basename='cart')

urlpatterns = [
    path('', include(router.urls))
]