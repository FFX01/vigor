from django.db import models
from django.conf import settings


class Program(models.Model):

    name = models.CharField(
        max_length=200,
        blank=False
    )

    styles = models.ManyToManyField(
        to='styles.Style',
        related_name='programs'
    )

    maintainers = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        related_name='maintained_programs'
    )

    followers = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        related_name='programs'
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

    @classmethod
    def can_create(cls, user):
        return user.is_authenticated()

    def can_read(self, user):
        return True

    def can_update(self, user):
        return user in self.maintainers()

    def can_delete(self, user):
        return user in self.maintainers()

    def maintainers(self):
        return self.program.maintainers.all()


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

    @classmethod
    def can_create(cls, user):
        return user.is_authenticated()

    def can_read(self, user):
        return True

    def can_update(self, user):
        return user in self.maintainers()

    def can_delete(self, user):
        return user in self.maintainers()

    def maintainers(self):
        return self.period.program.maintainers.all()


class Exercise(models.Model):

    name = models.CharField(
        max_length=400,
        blank=False
    )

    session = models.ForeignKey(
        to='programs.Session',
        related_name='exercises'
    )

    styles = models.ManyToManyField(
        to='styles.Style',
        related_name='exercises'
    )

    order = models.PositiveIntegerField(
        blank=False,
        default=1
    )

    sets = models.PositiveIntegerField(
        blank=True,
        default=1
    )

    weight = models.CharField(
        max_length=200,
        default="n/a"
    )

    duration = models.PositiveIntegerField(
        blank=True,
        default=1
    )

    notes = models.TextField()

    @classmethod
    def can_create(cls, user):
        return user.is_authenticated()

    def can_read(self, user):
        return True

    def can_update(self, user):
        return user in self.maintainers()

    def can_delete(self, user):
        return user in self.maintainers()

    def maintainers(self):
        return self.session.maintainers()
