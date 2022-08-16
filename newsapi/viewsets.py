from rest_framework import viewsets

from newsapi import models, serializers
from .models import News
from .serializers import NewsSerializer

class NewsViewset(viewsets.ModelViewSet):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer

