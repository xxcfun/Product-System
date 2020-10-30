from django.urls import path

from order import views
from order.views import OrderView

urlpatterns = [
    # 生产订单一览
    path('', OrderView.as_view(), name='order_all'),
    # 将订单加入生产流程控制页面
    path('detail/<int:pk>', views.order_detail, name='order_detail'),
]