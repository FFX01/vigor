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

    maintainers = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        related_name='maintained_styles'
    )

    created = models.DateField(
        auto_now_add=True,
        blank=True
    )

    updated = models.DateField(
        auto_now=True,
        blank=True
    )

    @classmethod
    def can_create(cls, user):
        return user.is_authenticated()

    def can_read(self, user):
        return True

    def can_update(self, user):
        return user in self.maintainers.all()

    def can_delete(self, user):
        return user in self.maintainers.all()

    def __str__(self):
        return "[Discipline][Name: {n}]".format(
            n=self.name
        )
