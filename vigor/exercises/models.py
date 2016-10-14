from django.db import models
from markupfield.fields import MarkupField
from django.conf import settings


class Exercise(models.Model):

    name = models.CharField(
        max_length=200,
        blank=False
    )

    description = MarkupField(
        markup_type='markdown',
        escape_html=True
    )

    discipline = models.ForeignKey(
        to='disciplines.Discipline',
        related_name='exercises'
    )

    creator = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name='created_exercises'
    )

    practitioners = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        related_name='practiced_exercises',
        through='exercises.ExercisePractice'
    )

    created = models.DateField(
        auto_now_add=True,
        blank=True
    )

    updated = models.DateField(
        auto_now=True,
        blank=True
    )


class ExercisePractice(models.Model):

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name='exercise_practices'
    )

    exercise = models.ForeignKey(
        to='exercises.Exercise',
        related_name='practices'
    )

    started = models.DateField(
        auto_now_add=True,
        blank=True
    )

    is_current = models.BooleanField(
        default=True,
        blank=True
    )

    ended = models.DateField(
        blank=True
    )

    notes = MarkupField(
        markup_type='markdown',
        escape_html=True
    )

    times_practiced = models.PositiveIntegerField(
        blank=True,
        default=0
    )
