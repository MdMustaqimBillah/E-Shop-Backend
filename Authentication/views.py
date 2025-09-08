from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from .repository import UserRepository
# Create your views here.


class RegistraitonViewSet(CreateAPIView):
    queryset = UserRepository().get_all()  # Use repository to get all users
    serializer_class = UserSerializer
    

class VerifyEmailView(APIView):
    def get(self, request, token):
        try:
            user = User.objects.get(email_verification_token=token)
            user.verify_email() # Calling verify_email from User model

            refresh = RefreshToken.for_user(user)

            return Response({
                "message": "Email verified. You are now logged in.",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)