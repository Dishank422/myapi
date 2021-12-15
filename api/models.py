from django.db import models
# Create your models here.


class Article(models.Model):
    sport = models.CharField(max_length=30)
    sex = models.CharField(max_length=1)
    type = models.CharField(max_length=30)
    level = models.CharField(max_length=1)
    team0 = models.CharField(max_length=1)
    team1 = models.CharField(max_length=1)
    date = models.DateField()
    time = models.TimeField()
    winner = models.CharField(max_length=1)
    timestamp = models.DateTimeField(auto_now=True)
