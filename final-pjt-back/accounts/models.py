from django.db import models
from django.contrib.auth.models import AbstractUser
from deposits.models import DepositProducts
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=20,unique=True)
    age = models.IntegerField(default=20)
    gender = models.IntegerField(default=1)
    salary = models.IntegerField(default=-1)
    wealth = models.IntegerField(default=-1)
    tendency = models.IntegerField(default=1)
    deposit = models.ManyToManyField(DepositProducts, blank=True, related_name="joined")
