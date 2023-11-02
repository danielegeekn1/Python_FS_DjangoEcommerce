from django.db import models
from django.contrib.sessions.models import Session
# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    provision = models.IntegerField()
    img_url = models.CharField(max_length=2083)
