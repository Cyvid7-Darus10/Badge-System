from django.db import models

class Badge(models.Model):
    label = models.CharField(max_length=250)
    date = models.CharField(max_length=50)
    points = models.IntegerField()
