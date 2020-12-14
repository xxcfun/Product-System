from django.urls import path

from order import views
from order.views import OrderView, OrderFinishView, OrderDeleteView, OrderAllView, OrderAllFinishView, \
    OrderAllDeleteView

urlpatterns = [
    # 业务
    # 待生产的生产订单
    path('', OrderView.as_view(), name='order'),
    # 已完成的生产订单
    path('finish/', OrderFinishView.as_view(), name='order_finish'),
    # 已删除的生产订单
    path('delete/', OrderDeleteView.as_view(), name='order_delete'),

    # 经理
    # 查看自己待生产的订单
    path('all/', OrderAllView.as_view(), name='order_all'),
    # 查看自己已完成的订单
    path('all_finish/', OrderAllFinishView.as_view(), name='order_all_finish'),
    # 查看自己已删除的订单
    path('all_delete/', OrderAllDeleteView.as_view(), name='order_all_delete'),

    # 商务
    path('seach/', views.order_seach, name='order_seach')

]