from django.db import models

# Create your models here.
class Book(models.Model):
    bookId = models.AutoField(primary_key=True)
    bookName = models.CharField(max_length=500)
    authorName = models.CharField(max_length=500)

