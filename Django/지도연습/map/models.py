from django.db import models

# Create your models here.
class LocationDetail(models.Model):
    locationid = models.CharField(max_length=20)
    locationname = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    relateurl = models.CharField(max_length=50)
    lat = models.CharField(max_length=20)
    lgt = models.CharField(max_length=20)
