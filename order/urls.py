from django.urls import path

from order import views
from order.views import OrderView, OrderFinishView, OrderDeleteView, OrderAllView, OrderAllFinishView, \
    OrderAllDeleteView, OrderAllBillView, OrderBillView

urlpatterns = [
    # 待生产的生产订单
    path('', OrderView.as_view(), name='order'),
    # 已完成的生产订单
    path('finish/', OrderFinishView.as_view(), name='order_finish'),
    # 已删除的生产订单
    path('delete/', OrderDeleteView.as_view(), name='order_delete'),
    # 查看所有待生产的订单
    path('all/', OrderAllView.as_view(), name='order_all'),
    # 查看所有已完成的订单
    path('all_finish/', OrderAllFinishView.as_view(), name='order_all_finish'),
    # 查看所有已删除的订单
    path('all_delete/', OrderAllDeleteView.as_view(), name='order_all_delete'),
    # 查看所有物流单号信息
    path('all_bill/', OrderAllBillView.as_view(), name='order_all_bill'),
    # 筛选订单
    path('seach/', views.order_seach, name='order_seach'),
    # 查询物流单号
    path('bill/', OrderBillView.as_view(), name='order_bill'),
    # 填写物流单号
    path('odd/<int:order_id>', views.order_odd, name='order_odd')
]