from django.urls import path

from order import views

urlpatterns = [
    # 所有生产订单
    path('', views.order_list, name='order_list'),
]