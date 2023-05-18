from rest_framework import serializers
from .models import DepositProducts, DepositOptions

class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('fin_prdt_cd',)

class DepositProductsSerializer(serializers.ModelSerializer):
    DepositOptions.fin_prdt_cd_set = DepositOptionsSerializer(many=True)
    
    class Meta:
        model = DepositProducts
        fields = '__all__'
