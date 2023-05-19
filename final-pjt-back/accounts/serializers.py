from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer

class CustomLoginSerializer(LoginSerializer):
    # email 필드 제거
    email = None

class CustomRegisterSerializer(RegisterSerializer):
    age = serializers.IntegerField()
    gender = serializers.IntegerField()
    salary = serializers.IntegerField()
    wealth = serializers.IntegerField()
    tendency = serializers.IntegerField()

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