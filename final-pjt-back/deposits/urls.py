from django.urls import path
from . import views

urlpatterns = [
    path('save/', views.save_deposit, name='deposit'),
    path('detail/<str:fin_prdt_cd>/', views.deposit_detail, name='depositdetail'),
    path('detail/<str:fin_prdt_cd>/<int:user_pk>/', views.deposit_sign, name='depositdetail'),
    path('recomend_deposit/', views.recomend_deposit, name='recomend_deposit'),
]