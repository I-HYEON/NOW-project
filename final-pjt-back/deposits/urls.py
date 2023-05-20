from django.urls import path
from . import views

urlpatterns = [
    path('save/', views.save_deposit, name='deposit'),
    path('detail/<str:fin_prdt_cd>', views.deposit_detail, name='depositdetail'),
    path('recomend_deposit/', views.recomend_deposit, name='recomend_deposit'),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('<int:depositproducts_pk>/comments/', views.comment_create),
]
