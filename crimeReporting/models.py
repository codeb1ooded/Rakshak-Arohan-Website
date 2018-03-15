from django.db import models

from django.contrib.auth.models import *

import datetime
# Create your models here.

STATUS_CHOICES = (
       ('lodged','LODGED'),
       ('pending','PENDING'),
       ('investigated','INVESTIGATED'),
       ('evidence_collection','EVIDENCE COLLECTION'),
       ('moved', 'MOVED TO COURT'),
       ('closed','CLOSED'),

    )

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
  DATE_CRIME = models.DateField((u"Conversation Date"), blank=True)
  TIME_CRIME = models.TimeField((u"Conversation Time"), blank=True)
  FIR_LOC = models.CharField(max_length=100)
  COMPLAINT_TIME = models.TimeField((u"Conversation Time"), blank=True)
  PHONE=models.CharField(max_length=100)
  STATUS = models.CharField(default='Lodged',choices = STATUS_CHOICES,max_length=100)


  def __str__(self):
      return self.CRIME_TYPE

class CRIME_TIMELINE(models.Model):
    CRIME_ID=models.ForeignKey(FIR_REPORT,on_delete=models.CASCADE)
    UPDATED_BY=models.ForeignKey(USER,on_delete=models.CASCADE)
    CURRENT_STATUS=models.CharField(default='Pending',choices = STATUS_CHOICES,max_length=100)
    TIME_OF_UPDATE=models.TimeField()
