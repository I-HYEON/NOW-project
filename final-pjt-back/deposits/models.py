from django.db import models
from accounts.models import User
# Create your models here.

class DepositProducts(models.Model):
    fin_prdt_cd = models.ManyToManyField(User,related_name='deposit_products')
    lcor_co_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()

class DepositOptions(models.Model):
    fin_prdt_cd = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    intr_rate_type_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField(default=-1)
    intr_rate2 = models.FloatField(default=-1)
    save_trm = models.IntegerField(default=-1)