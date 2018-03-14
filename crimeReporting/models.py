from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class USER(models.Model):
  USER_REF = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="USER")
  NAME = models.CharField(max_length=100)
  PASSWORD= models.CharField(max_length=6)

  def __str__(self):
      return self.NAME

class FIR_REPORT(models.Model):
  CRIME_TYPE = models.CharField(max_length=100)
  LOCATION_LAT = models.IntegerField()
  LOCATION_LONG = models.IntegerField()
  CRIME_DES = models.CharField(max_length=1000)

  def __str__(self):
      return self.CRIME_TYPE
  
  
