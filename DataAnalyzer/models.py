from django.db import models
from django.utils import timezone
# Create your models here.
class SensorData(models.Model):
    humidity = models.FloatField()
    temperature = models.FloatField()
    date = models.DateTimeField(default=timezone.now)

class Actuators(models.Model):
    name = models.CharField(max_length=200)
    status = models.ForeignKey('Status')

class Status(models.Model):
    name = models.CharField(max_length=200)
