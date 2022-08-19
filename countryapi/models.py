from django.db import models

# Create your models here.

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    ADMIN = models.CharField(max_length=500)
    Ease_of_Moving_Funds = models.CharField(max_length=500)
    Ease_of_Registration = models.CharField(max_length=500)
    Ease_of_fundraising_from_external_sources = models.CharField(max_length=500)
    Freedom_of_Assembly = models.CharField(max_length=500)
    Freedom_of_Expression = models.CharField(max_length=500)
    Presence_of_Laws_that_affect_CSOs = models.CharField(max_length=500)
    totalScore = models.CharField(max_length=500)
    averageScore = models.CharField(max_length=500)
    Primary_Laws_Affecting_CSOS = models.CharField(max_length=500)
    FeaturesOfTheLaw = models.CharField(max_length=500)
    flag = models.CharField(max_length=500)
    