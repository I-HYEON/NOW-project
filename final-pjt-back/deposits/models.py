from django.db import models
# Create your models here.

class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True) # 고유 코드
    fin_prdt_nm = models.TextField()            # 상품 명
    kor_co_nm = models.TextField()              # 은행 이름
    etc_note = models.TextField()               # 기타 정보  
    spcl_cnd = models.TextField()               # 우대
    mtrt_int = models.TextField()               # 만기 후~~
    join_deny = models.IntegerField()           # 가입 한도?
    join_member = models.TextField()            # 가입 인원?
    join_way = models.TextField()               # 가입 방법

class DepositOptions(models.Model):
    fin_prdt_cd = models.ForeignKey(DepositProducts, on_delete = models.CASCADE)
    intr_rate_type_nm = models.CharField(max_length=100)
    save_trm = models.IntegerField(default=-1)
    intr_rate = models.FloatField(default=-1)
    intr_rate2 = models.FloatField(default=-1)