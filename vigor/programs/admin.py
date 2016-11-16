from django.contrib import admin

from .models import Program, Period, Session, Exercise


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    pass


@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    pass


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    pass


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    pass
