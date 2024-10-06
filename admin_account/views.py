# admin_account/views.py
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import AdminAccount
from .serializers import CustomUserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = AdminAccount.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (AllowAny,)

class CustomTokenObtainPairView(TokenObtainPairView):
    # Anda dapat menyesuaikan data yang dikembalikan di sini jika perlu
    pass
