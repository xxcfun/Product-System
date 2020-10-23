from django.urls import path

from product import views
from product.views import ProdView, ProdListView, ProdSeachView

urlpatterns = [
    # 生产管理操作
    path('', ProdView.as_view(), name='prod'),
    # 生产信息筛选
    path('seach/', ProdSeachView.as_view(), name='prod_seach'),
    # 生产信息展示
    path('list/', ProdListView.as_view(), name='prod_list'),
]