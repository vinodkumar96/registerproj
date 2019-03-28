from django.db import models

# Create your models here.
class signup(models.Model):
    firstname = models.CharField(primary_key=True,max_length=30)
    lastname = models.CharField(max_length=30)
    dob = models.DateField()
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pincode = models.IntegerField()
    about = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    phnum = models.IntegerField()
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    confpass = models.CharField(max_length=10)
    answer = models.CharField(max_length=20)
class signin(models.Model):
    email = models.EmailField(max_length=30)
    username = models.CharField(max_length=10)
    phnum = models.IntegerField()
    password = models.CharField(max_length=10)