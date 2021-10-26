from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Application(models.Model):
    APPLICATION_TYPES = [
        ('comp', 'Zeitausgleich'),
        ('sick', 'Krankenstand'),
        ('vacation', 'Urlaub'),
    ]
    STATUS_TYPES = [
        ('accepted', 'Akzeptiert'),
        ('pending', 'Austehend'),
        ('denied', 'Abgelehnt'),
    ]

    user_id = models.IntegerField(blank=False)
    description = models.TextField(max_length=160, blank=True, default='')
    type = models.CharField(
        max_length=10,
        choices=APPLICATION_TYPES,
        default='vacation',
        blank=False
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_TYPES,
        default='pending',
        blank=False
    )
    reviewed_by = models.IntegerField(blank=True, default=0)
    start_date = models.DateField(blank=False)
    start_time = models.TimeField(blank=True, null=True)
    end_date = models.DateField(blank=False)
    end_time = models.TimeField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=False)

    class Meta:
        verbose_name = 'Application'
        verbose_name_plural = verbose_name

    @property
    def user(self):
        return User.objects.get(pk=self.user_id)

