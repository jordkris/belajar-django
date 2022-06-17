from django.db import models

# Create your models here.
class User(models.Model):
    userName = models.CharField(primary_key=True,max_length=50)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    dob = models.DateField()
    phoneNumber = models.IntegerField()

class Customer(models.Model):
    name = models.CharField(primary_key=True,max_length=50)
    age = models.IntegerField()
    dateOfBirth = models.DateField()
    accountNumber = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    

