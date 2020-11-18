from django.urls import path

from user import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    # 用户中心
    path('mine/', views.mine, name='mine'),
    # path('list/', views.list, name='list'),
    # path('edite/?P<>', views.edite, name='edite'),
]
