from django.db import models

# Create your models here.
class Hike(models.Model):
    name = models.CharField(max_length=30)
    duration = models.IntegerField()
    description = models.CharField(max_length=30, blank=True)
    length = models.FloatField()
    location = models.CharField(max_length=30)

    def __str__(self) -> str:
        return ("Hike: " + self.name + "\n\t" + "Duration: " + self.duration + "\n\t" + "Description: " + self.description + "\n\t" + "Length: " + self.length + "\n\t" + "Location: " + self.location)

class Hiker(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    birthday = models.DateField()

    @property
    def full_name(self):
        return (self.firstname + " " + self.lastname)

    def __str__(self) -> str:
        return ("User: " + self.username + "\n\tFirstname: " + self.firstname + "\n\tLastname: " + self.lastname + "\n\tEmail: " + self.email)
