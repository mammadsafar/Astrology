from django.db import models

from django.contrib.auth.models import User

'''
I have 3 models in this file:
- Country
- province
- City
'''

class Country(models.Model):
    name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=20)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Province(models.Model):
    name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100, blank=True, null=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " - " + self.province.name


