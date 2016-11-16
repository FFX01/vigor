from django.db import models
from django.conf import settings


class Style(models.Model):

    name = models.CharField(
        max_length=250,
        blank=False
    )

    description = models.TextField(
        blank=True
    )

    creator = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name='created_disciplines'
    )

    created = models.DateField(
        auto_now_add=True,
        blank=True
    )

    updated = models.DateField(
        auto_now=True,
        blank=True
    )

    def __str__(self):
        return "[Discipline][Name: {n}]".format(
            n=self.name
        )
