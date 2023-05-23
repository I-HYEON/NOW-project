from dj_rest_auth.serializers import LoginSerializer,UserDetailsSerializer
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
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['pk','username', 'age', 'gender','salary', 'wealth', 'tendency', 'deposit']

class CustomUserDetailsSerializer(UserDetailsSerializer):
    age = serializers.IntegerField(required=False, allow_null=True)
    gender = serializers.IntegerField(required=False, allow_null=True)
    salary = serializers.IntegerField(required=False, allow_null=True)
    wealth = serializers.IntegerField(required=False, allow_null=True)
    tendency = serializers.IntegerField(required=False, allow_null=True)
    
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('age', 'gender', 'salary', 'wealth', 'tendency', 'deposit')
    
    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()

        data_dict['age'] = self.validated_data.get('age', None)
        data_dict['gender'] = self.validated_data.get('gender', None)
        data_dict['salary'] = self.validated_data.get('salary', None)
        data_dict['wealth'] = self.validated_data.get('wealth', None)
        data_dict['tendency'] = self.validated_data.get('tendency', None)
        
        return data_dict
    
    def update(self, instance, validated_data):
            
        instance = super().update(instance, validated_data)
        # instance.username = validated_data.get('username', None)
        instance.age = validated_data.get('age', None)
        instance.gender = validated_data.get('gender', None)
        instance.salary = validated_data.get('salary', None)
        instance.wealth = validated_data.get('wealth', None)
        instance.tendency = validated_data.get('tendency', None)
        instance.save()
        return instance
    
    def save(self):
        # self.validated_data.pop('username', None)
        user = super().save()
        user.age = self.validated_data.get('age', None)
        user.gender = self.validated_data.get('gender', None)
        user.salary = self.validated_data.get('salary', None)
        user.wealth = self.validated_data.get('wealth', None)
        user.tendency = self.validated_data.get('tendency', None)
        user.save()
        return user