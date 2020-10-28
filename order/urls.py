from django.urls import path

from order import views

urlpatterns = [
    # 生产订单一览
    path('', views.order_all, name='order_all'),
]