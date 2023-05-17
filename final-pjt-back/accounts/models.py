from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=50,unique=True)
    age = models.IntegerField()
    gender = models.IntegerField()
    salary = models.IntegerField()
    wealth = models.IntegerField()
    tendency = models.IntegerField()