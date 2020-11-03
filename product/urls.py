from django.urls import path

from product import views
from product.views import BLView, SCZView, DFHView, DDWCView, ProdView

urlpatterns = [
    # 所有生产订单
    path('', ProdView.as_view(), name='product_all'),
    # 生产人员将订单加入生产列表
    path('add/<int:pk>', views.prod_add, name='prod_add'),
    # 生产过程查询
    path('seach/', views.product_seach, name='product_seach'),
    # 备料阶段
    path('BL/', BLView.as_view(), name='product_bl'),
    # 生产中阶段
    path('SCZ/', SCZView.as_view(), name='product_scz'),
    # 待发货阶段
    path('DFH/', DFHView.as_view(), name='product_dfh'),
    # 订单完成阶段
    path('DDWC/', DDWCView.as_view(), name='product_ddwc'),
    # 更改生产状态
    path('edit/<int:pk>', views.product_edit, name='product_edit'),
]
