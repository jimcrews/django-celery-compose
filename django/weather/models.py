from django.db import models

class Forecast(models.Model):
    stream_id = models.CharField(max_length=50)
    date = models.CharField(max_length=8)
    temperature = models.IntegerField()
    summary = models.CharField(max_length=50)
    fire_danger = models.CharField(max_length=50)
