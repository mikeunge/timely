from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('', include('timely.urls')),
	path('stats/', include('statistic.urls')),
    path('admin/', admin.site.urls),
]
