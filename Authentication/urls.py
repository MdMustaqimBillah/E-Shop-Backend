from django.urls import path
from Authentication.views import RegistraitonViewSet, VerifyEmailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/", RegistraitonViewSet.as_view(), name="register"),
    path("verify-email/<str:token>/", VerifyEmailView.as_view(), name="verify-email"),
    path("login/", TokenObtainPairView.as_view(), name="login"),   # JWT login
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
