from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # application routes
    path('', views.application, name='application'),
    path('viewall/', views.view_all, name='all_applications'),
    path('view/<int:application>', views.application, name='one_application'),
    path('create/<int:application>', views.application, name='create_application'),
    path('delete/<int:application>', views.application, name='delete_applicaion'),
    path('accept/<int:application>', views.application, name='accept_application'),
    path('deny/<int:application>', views.application, name='deny_application'),
]
