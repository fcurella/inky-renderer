from django.db import models

from django_extensions.db.models import TimeStampedModel


class Screen(TimeStampedModel):
    name = models.CharField(max_length=255)
    image = models.ImageField()
