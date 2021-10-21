from django.db import models

TRACK_TYPES = [
    ('wo', 'Arbeit'),
    ('br', 'Pause'),
]

class Timer(models.Model):
    user_id = models.IntegerField(blank=False)
    date = models.DateField(auto_now_add=True, blank=False)
    type = models.CharField(
        max_length=2,
        choices=TRACK_TYPES,
        default='wo',
        blank=False
    )
    is_running = models.BooleanField(default=True)
    time_total = models.CharField(default="", max_length=16)
    start_time = models.TimeField(auto_now_add=True, blank=False)
    stop_time = models.TimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return str(self.date)

