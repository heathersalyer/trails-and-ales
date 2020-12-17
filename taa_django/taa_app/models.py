from django.db import models
from django.contrib.auth.models import User

class Hike(models.Model):
    hike_name = models.CharField(max_length=200)
    summary = models.CharField(max_length=500)
    location = models.CharField(max_length=250)
    distance = models.IntegerField()
    difficulty = models.CharField(max_length=30)

    def __str__(self):
        return self.hike_name

class Brewery(models.Model):
    brewery_name = models.CharField(max_length=250)
    type = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    address3 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    phone = models.CharField(max_length=11)
    website = models.CharField(max_length=100)

    def __str__(self):
        return self.brewery_name



