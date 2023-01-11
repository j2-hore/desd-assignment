from django.db import models

# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=50)
    age_rating = models.CharField(max_length=3)
    duration = models.IntegerField() #Give the runtime in minutes
    trailer_description = models.CharField(max_length=150)

class Club(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    contacts = models.IntegerField() #Landline, mobile and e-Mail
    representative = models.CharField(max_length=150) #First name, last name and date of birth.

class Screen(models.Model):
    capacity = models.IntegerField()
    seat_number = models.IntegerField()
    social_dist = models.CharField(max_length=3) 

class Showing(models.Model):
    title = models.CharField(max_length=50)
    date = models.CharField(max_length=10)
    time = models.CharField(max_length =10)
