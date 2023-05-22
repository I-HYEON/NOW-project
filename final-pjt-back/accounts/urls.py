from django.urls import path,include
from .views import CustomRegisterView, CustomUserDetailsView, user_info

urlpatterns = [
    path('signup/', CustomRegisterView.as_view(), name='account_signup'),
    path('user/', CustomUserDetailsView.as_view(), name='account_userinfo'),
    path('user_info/',user_info,name="user_info"),
    path('', include('dj_rest_auth.urls')),
]