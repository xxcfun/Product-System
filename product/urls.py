from django.urls import path

from product import views

urlpatterns = [
    # 生产流程控制
    path('', views.product_all, name='product_all')
    # 更改生产订单状态
    # path('edit/<int:pk>', views.prod_edit, name='prod_edit'),
    # 销毁订单
    # path('del/<int:pk>', views.prod_del, name='prod_del')
]