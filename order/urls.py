from django.urls import path

from order import views
from order.views import OrderView, OrderFinishView, OrderDeleteView

urlpatterns = [
    # 待生产的生产订单
    path('', OrderView.as_view(), name='order'),
    # 已完成的生产订单
    path('finish/', OrderFinishView.as_view(), name='order_finish'),
    # 已删除的生产订单
    path('delete/', OrderDeleteView.as_view(), name='order_delete'),
    # 删除订单
    path('delect/<int:order_id>', views.order_del, name='order_del'),
    # 查看自己待生产的订单
    path('owen/', views.order_mine, name='order_mine'),
    # 查看自己已完成的订单
    path('owen_finish/', views.order_mine_finish, name='order_mine_finish'),
    # 查看自己已删除的订单
    path('owen_delete/', views.order_mine_delete, name='order_mine_delete'),
]