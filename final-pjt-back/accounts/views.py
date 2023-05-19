# from django.shortcuts import render
from dj_rest_auth.views import LoginView
from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomLoginSerializer, CustomRegisterSerializer

class CustomLoginView(LoginView):
    serializer_class = CustomLoginSerializer

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer