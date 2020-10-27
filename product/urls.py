from django.urls import path

from product import views
from product.views import ProdListView

urlpatterns = [
    # 生产所有
    # path('all/', views.prod_all, name='prod_all'),
    path('BL/', views.prod_bl, name='prod_bl'),
    path('PD/', views.prod_pd, name='prod_pd'),
    path('SCZ/', views.prod_scz, name='prod_scz'),
    path('DFH/', views.prod_dfh, name='prod_dfh'),
    path('DDWC/', views.prod_ddwc, name='prod_ddwc'),
    # 生产信息筛选
    path('seach/', views.seach, name='prod_seach'),
    # 生产信息展示
    path('list/', ProdListView.as_view(), name='prod_list'),
    # 更改生产订单状态
    path('edit/<int:pk>', views.prod_edit, name='prod_edit'),
    # 销毁订单
    path('del/<int:pk>', views.prod_del, name='prod_del')
]