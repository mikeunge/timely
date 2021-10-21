from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', views.signin, name='login'),
    path('accounts/logout/', views.signout, name='logout'),
    path('accounts/change-password/', views.change_password, name='change_password'),
    path('timer/start/<str:method>/', views.timer_start, name='timer_start'),
    path('timer/stop/', views.timer_stop, name='timer_stop'),
]
