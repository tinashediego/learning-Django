from django.shortcuts import render
from rest_framework.response import Response

from .serializers import RegisterSerializer

from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework import generics

class RegisterApi(generics.GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        return Response({"user": RegisterSerializer(user, context=self.get_serializer_context()).data,"message": "User Created Successfully. Now perform Login to get your token",})