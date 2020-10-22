from django.urls import path

from product import views

urlpatterns = [
    # 生产管理操作
    path('', views.prod, name='prod'),
    # 生产信息筛选
    path('seach/', views.prod_seach, name='prod_seach'),
    # 生产信息展示
    path('list/', views.prod_list, name='prod_list'),
]