from django.db import models
from django.contrib.auth.models import User

class Timer(models.Model):
    TRACK_TYPES = [
        ('work', 'Arbeit'),
        ('break', 'Pause'),
    ]

    user_id = models.IntegerField(blank=False)
    start_date = models.DateField(auto_now_add=True, blank=False)
    end_date = models.DateField(auto_now_add=True, blank=False)
    type = models.CharField(
        max_length=10,
        choices=TRACK_TYPES,
        default='work',
        blank=False
    )
    is_running = models.BooleanField(default=True)
    time_total = models.CharField(default='', max_length=16)
    start_time = models.TimeField(auto_now_add=True, blank=False)
    stop_time = models.TimeField(auto_now_add=True, blank=False)

    class Meta:
        verbose_name = 'Timer'
        verbose_name_plural = verbose_name

    @property
    def user(self):
        return User.objects.get(pk=self.user_id)


class UserSettings(models.Model):
    user_id = models.IntegerField(blank=False, primary_key=True)
    work_hours_per_week = models.DecimalField(blank=False, default=40, max_digits=4, decimal_places=2)
    timer_seconds = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'User Settings'
        verbose_name_plural = verbose_name

    @property
    def user(self):
        return User.objects.get(pk=self.user_id)

