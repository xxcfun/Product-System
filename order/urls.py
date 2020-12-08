from django.urls import path

from order import views
from order.views import OrderView, OrderFinishView

urlpatterns = [
    # 所有生产订单
    path('', OrderView.as_view(), name='order'),
    path('finish/', OrderFinishView.as_view(), name='order_finish'),
    # 所有生产订单
    # path('', views.order, name='order_list'),
    # path('finish/', views.order_finish, name='order_finish'),
    # 删除订单
    path('delect/<int:order_id>', views.order_del, name='order_del'),
    # 查看自己的订单
    path('owen/', views.order_mine, name='order_mine'),
]