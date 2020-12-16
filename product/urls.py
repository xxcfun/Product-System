from django.urls import path

from product import views
from product.views import ProOrderView, ProduceView, DeliverView, FinishView

urlpatterns = [
    # 将订单加入生产流程控制页面
    path('detail/<int:order_id>', views.order_detail, name='order_detail'),
    # 生产人员将订单加入生产列表
    path('add/<int:order_id>', views.prod_add, name='prod_add'),
    # 生产人员将订单删除
    path('del/<int:order_id>', views.prod_del, name='prod_del'),
    # 待生产订单
    path('order/', ProOrderView.as_view(), name='prod_order'),
    # # 备料阶段
    # path('material/', MaterialView.as_view(), name='prod_material'),
    # 生产中阶段
    path('produce/', ProduceView.as_view(), name='prod_produce'),
    # 待发货阶段
    path('deliver/', DeliverView.as_view(), name='prod_deliver'),
    # 订单完成阶段
    path('finish/', FinishView.as_view(), name='prod_finish'),
    # 更改生产状态
    path('edit/<int:order_id>', views.prod_edit, name='prod_edit'),

    # 下面都为批量操作
    # 批量删除
    path('delall/', views.prod_del_all, name='prod_del_all'),
    # 批量生产进入生产列表
    path('addall/', views.prod_add_all, name='prod_add_all'),
    # 批量更改生产状态
    path('editall/', views.prod_edit_all, name='prod_edit_all'),
]
