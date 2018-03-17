from django.db import models

from django.contrib.auth.models import *
from django.utils.timezone import now
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
  ID= models.AutoField(null=False,primary_key=True)
  CRIME_TYPE = models.CharField(max_length=100)
  LAT = models.FloatField()
  LNG = models.FloatField()
  CRIME_DESCRIPTION = models.CharField(null=True,max_length=1000,blank=True)
  PERSON_COMPLAINT = models.ForeignKey(USER,on_delete=models.CASCADE)
  COMPLAINT_BY = models.CharField(max_length=100)
  DATE_CRIME = models.DateField()
  TIME_CRIME = models.TimeField()
  FIR_LOC = models.CharField(max_length=100)
  COMPLAINT_TIME = models.TimeField()
  PHONE=models.CharField(max_length=100)
  STATUS = models.CharField(default='Lodged',choices = STATUS_CHOICES,max_length=100)


  def __str__(self):
      return str(self.ID)

class CRIME_TIMELINE(models.Model):
    CRIME_ID=models.ForeignKey(FIR_REPORT,on_delete=models.CASCADE)
    UPDATED_BY=models.ForeignKey(USER,on_delete=models.CASCADE)
    CURRENT_STATUS=models.CharField(default='Pending',choices = STATUS_CHOICES,max_length=100)
    TIME_OF_UPDATE=models.DateTimeField(default=now(), blank=True)
    DESCRIPTION=models.CharField(null=True,default="Pending",max_length=1000,blank=True)