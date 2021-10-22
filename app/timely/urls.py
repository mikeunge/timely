from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . import services

urlpatterns = [
    path('', views.index, name='index'),
    # account related routes
    path('accounts/login/', views.signin, name='login'),
    path('accounts/logout/', views.signout, name='logout'),
    path('accounts/change-password/', views.change_password, name='change_password'),
    # timer routes
    path('timer/start/<str:method>/', views.timer_start, name='timer_start'),
    path('timer/stop/', views.timer_stop, name='timer_stop'),
    # api routes below
    path('api/timer/<int:user>/', services.get_total_time, name='get_total_timer'),
]
