from django.urls import path,include
from .views import CustomRegisterView, user_info, user_delete, user_check, CustomUserDetailsView, change_password
from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer

urlpatterns = [
    path('signup/', CustomRegisterView.as_view(), name='account_signup'),
    path('user/', CustomUserDetailsView.as_view(), name='account_userinfo'),
    path('user_info/',user_info,name="user_info"),
    path('', include('dj_rest_auth.urls')),
    path('signup/', CustomRegisterView.as_view(),name="rest_register"),
    path('delete/', user_delete, name='user_delete'),
    path('check/', user_check,),
    path('changepassword/', change_password,),
]