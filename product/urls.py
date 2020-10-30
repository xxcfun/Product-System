from django.urls import path

from product import views
from product.views import BLView, SCZView, DFHView, DDWCView

urlpatterns = [
    # 生产流程控制
    path('', views.product_all, name='product_all'),
    # 订单加入生产列表
    path('add/<int:pk>', views.prod_add, name='prod_add'),
    # 订单查询
    path('seach/', views.product_seach, name='product_seach'),
    # 备料
    path('BL/', BLView.as_view(), name='product_bl'),
    # 生产中
    path('SCZ/', SCZView.as_view(), name='product_scz'),
    # 待发货
    path('DFH/', DFHView.as_view(), name='product_dfh'),
    # 订单完成
    path('DDWC/', DDWCView.as_view(), name='product_ddwc'),
    # 订单状态转换
    path('edit/<int:pk>', views.product_edit, name='product_edit'),
]
