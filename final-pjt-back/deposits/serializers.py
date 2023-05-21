from rest_framework import serializers
from .models import DepositProducts, DepositOptions, Comment

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

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('depositproducts','user')

class DepositProductsSerializerC(serializers.ModelSerializer):
    DepositOptions.fin_prdt_cd_set = DepositOptionsSerializer(many=True)
    user_count = serializers.SerializerMethodField()

    def get_user_count(self, obj):
        temp = DepositProducts.objects.get(fin_prdt_cd=obj['fin_prdt_cd'])
        return temp.joined.count()
    
    class Meta:
        model = DepositProducts
        fields = '__all__'

class DepositProductsSerializerD(serializers.ModelSerializer):
    DepositOptions.fin_prdt_cd_set = DepositOptionsSerializer(many=True)
    user_count = serializers.SerializerMethodField()

    def get_user_count(self, obj):
        return obj.joined.count()
    
    class Meta:
        model = DepositProducts
        fields = '__all__'
