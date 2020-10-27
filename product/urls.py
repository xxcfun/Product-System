from django.urls import path

from product import views
from product.views import ProdListView

urlpatterns = [
    # 生产管理操作
    path('', views.prod, name='prod'),
    # 生产信息筛选
    path('seach/', views.seach, name='prod_seach'),
    # 生产信息展示
    path('list/', ProdListView.as_view(), name='prod_list'),
    # 更改生产订单状态
    path('edit/<int:pk>', views.edit, name='prod_edit')
]