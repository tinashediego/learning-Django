from django.db import models

# Create your models here.
class News(models.Model):
    newsId = models.AutoField(primary_key=True)
    newsTitle = models.CharField(max_length=500)
    readerName = models.CharField(max_length=500)

