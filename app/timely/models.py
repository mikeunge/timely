from django.db import models
from django.contrib.auth.models import User

TRACK_TYPES = [
    ('work', 'Arbeit'),
    ('break', 'Pause'),
]

class Timer(models.Model):
    user_id = models.IntegerField(blank=False)
    date = models.DateField(auto_now_add=True, blank=False)
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
    user_id = models.IntegerField(blank=False)
    timer_seconds = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'User Settings'
        verbose_name_plural = verbose_name

    @property
    def user(self):
        return User.objects.get(pk=self.user_id)

