# from django.shortcuts import render
from dj_rest_auth.views import LoginView, UserDetailsView
from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomLoginSerializer, CustomRegisterSerializer, CustomUserDetailsSerializer, UserSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import User
from django.contrib.auth.hashers import check_password


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

@api_view(['POST'])
def user_delete(request):
    user = request.user
    password = request.data.get('password1', None)  # Vue에서 보낸 비밀번호

    if user.is_authenticated:
        # 저장된 비밀번호와 입력된 비밀번호 일치 여부 확인
        if password and check_password(password, user.password):
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['POST'])
def change_password(request):
    user = request.user
    old_password = request.data.get('old_password', None)  # 이전 비밀번호
    new_password = request.data.get('new_password', None)  # 새로운 비밀번호

    if user.is_authenticated:
        # 이전 비밀번호와 현재 비밀번호가 일치하는지 확인
        if old_password and check_password(old_password, user.password):
            if new_password:
                user.set_password(new_password)
                user.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response({'error': 'New password is required'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Invalid old password'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_check(request):
    user = request.user
    password = User.objects.get(username=request.user).password
    print(user)
    print(password)
    return Response(status=status.HTTP_204_NO_CONTENT)

