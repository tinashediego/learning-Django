from django.urls import path, include
from .api import SimpleApI
urlpatterns = [
    path('hello', SimpleApI.as_view() ),
]