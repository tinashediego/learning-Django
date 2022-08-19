from rest_framework import viewsets

from countryapi import models, serializers
from .serializers import CountrySerializer

class CountryViewset(viewsets.ModelViewSet):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer

