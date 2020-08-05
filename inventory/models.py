from django.db import models


from django_extensions.db.models import TimeStampedModel


class Screen(TimeStampedModel):
    BORDER_CHOICES = (
        (0, "white"),
        (1, "black"),
        (2, "yellow"),
        (2, "red"),
    )
    name = models.CharField(max_length=255)
    image = models.ImageField()
    border = models.PositiveSmallIntegerField(choices=BORDER_CHOICES, default=0)
