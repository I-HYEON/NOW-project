from django.urls import path,include
from .views import CustomRegisterView, CustomUserDetailsView

urlpatterns = [
    path('signup/', CustomRegisterView.as_view(), name='account_signup'),
    path('user/', CustomUserDetailsView.as_view(), name='account_userinfo'),
    path('', include('dj_rest_auth.urls')),
]