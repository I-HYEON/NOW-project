from dj_rest_auth.serializers import LoginSerializer
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

class CustomLoginSerializer(LoginSerializer):
    # email 필드 제거
    email = None

class CustomRegisterSerializer(RegisterSerializer):
    age = serializers.IntegerField(required=False, allow_null=True)
    gender = serializers.CharField(required=False, allow_blank=True)
    salary = serializers.IntegerField(required=False, allow_null=True)
    wealth = serializers.IntegerField(required=False, allow_null=True)
    tendency = serializers.IntegerField(required=False, allow_null=True)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['age'] = self.validated_data.get('age', None)
        data_dict['gender'] = self.validated_data.get('gender', None)
        data_dict['salary'] = self.validated_data.get('salary', None)
        data_dict['wealth'] = self.validated_data.get('wealth', None)
        data_dict['tendency'] = self.validated_data.get('tendency', None)
        
        return data_dict
    
    def save(self, request):
        user = super().save(request)
        user.age = self.validated_data.get('age', None)
        user.gender = self.validated_data.get('gender', None)
        user.salary = self.validated_data.get('salary', None)
        user.wealth = self.validated_data.get('wealth', None)
        user.tendency = self.validated_data.get('tendency', None)
        user.save()
        return user