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
    userName = models.CharField(primary_key=True,max_length=50)
    name = models.CharField(max_length=50)
    dateOfBirth = models.DateField()
    accountNumber = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    

