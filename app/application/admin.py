from django.contrib import admin
from django.contrib.auth.models import User
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    model = Application
    list_display = ("user","type","status")
