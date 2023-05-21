from django.urls import path,include
from . import views

urlpatterns = [
    path('<str:words>/', views.search, name='search'),
]
