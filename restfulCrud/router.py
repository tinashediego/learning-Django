from bookapi.viewsets import BookViewset
from newsapi.viewsets import NewsViewset
from rest_framework import routers



router = routers.DefaultRouter()
router.register('book',BookViewset)
router.register('news',NewsViewset)