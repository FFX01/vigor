from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import less_than_1000_validator


class User(AbstractUser):

    height = models.PositiveIntegerField(
        verbose_name="Height",
        help_text="In Centimeters",
        blank=True,
        default=0,
        validators=[less_than_1000_validator]
    )

    weight = models.PositiveIntegerField(
        verbose_name="Weight",
        help_text="In Kilograms",
        blank=True,
        default=0,
        validators=[less_than_1000_validator]
    )
