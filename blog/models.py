from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)

    def __str__(self):
        return self.title

