from rest_framework import viewsets

from bookapi import models, serializers
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated
class BookViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

