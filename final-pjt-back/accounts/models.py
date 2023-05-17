from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    username = models.CharField()
    age = models.IntegerField()
    gender = models.IntegerField()
    salary = models.IntegerField()
    wealth = models.IntegerField()
    tendency = models.IntegerField()