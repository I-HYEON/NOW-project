# from django.shortcuts import render
from dj_rest_auth.views import LoginView, UserDetailsView
from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomLoginSerializer, CustomRegisterSerializer, CustomUserDetailsSerializer, UserSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class CustomLoginView(LoginView):
    serializer_class = CustomLoginSerializer

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def user_info(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)

class CustomUserDetailsView(UserDetailsView):
    serializer_class = CustomUserDetailsSerializer
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()