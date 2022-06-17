from django.db import models

# Create your models here.
class User(models.Model):
    userName = models.CharField(primary_key=True,max_length=50)
    fullName = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    dateRegistered = models.DateField()
    exp = models.IntegerField()
    
class Reksadana(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    unitPrice = models.CharField(max_length=50)
    unitNumber = models.IntegerField()
    userName = models.ForeignKey(User, on_delete=models.CASCADE)