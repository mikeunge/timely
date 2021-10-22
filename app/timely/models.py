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
    time_total = models.CharField(default="", max_length=16)
    start_time = models.TimeField(auto_now_add=True, blank=False)
    stop_time = models.TimeField(auto_now_add=True, blank=False)

    @property
    def user(self):
        return User.objects.get(pk=self.user_id)

    def __str__(self):
        type = self.type
        while len(type) < 5:
            type += ' '
        return f'[{type}] {str(self.date)} :: {self.user} - {self.time_total}'
