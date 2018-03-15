from django.db import models

from django.contrib.auth.models import *

import datetime
# Create your models here.


class USER(models.Model):
  USER_REF = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="USER")
  NAME = models.CharField(max_length=100)
  PASSWORD= models.CharField(max_length=6)

  def __str__(self):
      return self.NAME

class FIR_REPORT(models.Model):
  CRIME_TYPE = models.CharField(max_length=100)
  LAT = models.FloatField()
  LNG = models.FloatField()
  CRIME_DESCRIPTION = models.CharField(max_length=1000)
  PERSON_COMPLAINT = models.ForeignKey(USER,on_delete=models.CASCADE)
  COMPLAINT_BY = models.CharField(max_length=100)
  DATE_CRIME = models.DateField()
  TIME_CRIME = models.TimeField()
  FIR_LOC = models.CharField(max_length=100)
  COMPLAINT_TIME = models.TimeField()
  PHONE=models.CharField(max_length=100)
  STATUS = models.CharField(default='Pending',max_length=100)


  def __str__(self):
      return self.CRIME_TYPE
