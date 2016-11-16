from django.db import models


class Program(models.Model):

    name = models.CharField(
        max_length=200,
        blank=False
    )

    styles = models.ManyToManyField(
        to='styles.Style',
        related_name='programs'
    )

    practitioners = models.ManyToManyField(
        to='users.User',
        related_name='programs'
    )

    def __str__(self):
        return "[Program: {p}]".format(
            p=self.name
        )


class Period(models.Model):

    number = models.PositiveIntegerField(
        blank=False,
        default=1
    )

    description = models.TextField()

    program = models.ForeignKey(
        to='programs.Program',
        related_name='periods'
    )


class Session(models.Model):

    number = models.PositiveIntegerField(
        blank=False,
        default=1
    )

    description = models.TextField()

    period = models.ForeignKey(
        to='programs.Period',
        related_name='sessions'
    )


class Exercise(models.Model):

    order = models.PositiveIntegerField(
        blank=False,
        default=1
    )

    sets = models.PositiveIntegerField(
        blank=True,
        default=1
    )

    weight = models.PositiveIntegerField(
        blank=True,
        default=1
    )

    duration = models.PositiveIntegerField(
        blank=True,
        default=1
    )

    notes = models.TextField()
