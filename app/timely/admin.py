from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Timer, UserSettings

@admin.register(Timer)
class TimerAdmin(admin.ModelAdmin):
    model = Timer
    list_display = ("user","type","start_time","stop_time","time_total","is_running")

    def make_active(modeladmin, request, queryset):
        queryset.update(is_running = 1)
        messages.success(request, 'Selected record(s) marked as active successfully!')
  
    def make_inactive(modeladmin, request, queryset):
        queryset.update(is_running = 0)
        messages.success(request, 'Selected record(s) marked as inactive successfully!')
  
    admin.site.add_action(make_active, 'Start')
    admin.site.add_action(make_inactive, 'Stop')


@admin.register(UserSettings)
class UserSettingsAdmin(admin.ModelAdmin):
    model = UserSettings
    list_display = ("user","work_hours_per_week")
