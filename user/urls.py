from django.urls import path

from user import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    # path('list/', views.list, name='list'),
    # path('edite/?P<>', views.edite, name='edite'),
]
