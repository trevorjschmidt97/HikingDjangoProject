from django.db import models

# Create your models here.

class Hike(models.Model):
    hikerName = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    duration = models.IntegerField()
    description = models.CharField(max_length=30, blank=True)
    length = models.FloatField()
    location = models.CharField(max_length=30)

    def __str__(self) -> str:
        return ("Hike: " + self.name)
