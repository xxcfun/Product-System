from django.urls import path

from order.views import ProdOrderView

urlpatterns = [
    # 所有生产订单
    path('', ProdOrderView.as_view(), name='order_list'),
]