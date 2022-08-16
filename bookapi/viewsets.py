from rest_framework import viewsets

from bookapi import models, serializers
from .models import Book
from .serializers import BookSerializer

class BookViewset(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

