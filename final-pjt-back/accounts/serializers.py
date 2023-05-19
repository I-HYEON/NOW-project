from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer

class CustomLoginSerializer(LoginSerializer):
    # email 필드 제거
    email = None

class CustomRegisterSerializer(RegisterSerializer):
    age = serializers.IntegerField()
    gender = serializers.CharField()
    salary = serializers.IntegerField()
    wealth = serializers.IntegerField()
    tendency = serializers.IntegerField()

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['age'] = self.validated_data.get('age', '')
        data_dict['gender'] = self.validated_data.get('gender', '')
        data_dict['salary'] = self.validated_data.get('salary', '')
        data_dict['wealth'] = self.validated_data.get('wealth', '')
        data_dict['tendency'] = self.validated_data.get('tendency', '')
        
        return data_dict