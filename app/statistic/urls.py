from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # the app/urls send the request to this router if stats/* is prefixed
    path('', views.stats_index, name='stats_index'),
]
