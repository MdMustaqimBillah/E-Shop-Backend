from django.shortcuts import render
from restframework import viewsets
from restframework.generics import CreateView
from .models import User
# Create your views here.


class RegistraionViewSet(CreateView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
    def perform_create(self, serializer):
        serializer.save()
        return super().perform_create(serializer)
    return super().perform_create(serializer)

    
class VerifyEmailView(APIView):
    def get(self, request, token):
        try:
            user = User.objects.get(email_verification_token=token)
            user.is_active = True
            user.is_verified = True
            user.email_verification_token = None
            user.save()
            return Response({"message": "Email verified. You can now log in."}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)