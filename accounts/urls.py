from rest_framework import viewsets

from accounts import serializers
from django.contrib.auth.models import User
#from .serializers import RegistrationSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny, IsAdminUser
class RegistrationViewset(viewsets.ModelViewSet):
    permission_classes = (AllowAny)
    queryset = User.objects.all()
    serializer_class = serializers.RegistrationSerializer
