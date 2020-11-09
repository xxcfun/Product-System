from django.urls import path

from order import views
from order.views import OrderListView

urlpatterns = [
    # 所有生产订单
    path('', OrderListView.as_view(), name='order_list'),
]