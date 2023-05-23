from django.urls import path,include
from .views import CustomRegisterView, user_info, user_delete, user_check
from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('signup/', CustomRegisterView.as_view(),name="rest_register"),
    path('user_info/',user_info, name="user_info"),
    path('delete/', user_delete, name='user_delete'),
    path('check/', user_check,),
]
