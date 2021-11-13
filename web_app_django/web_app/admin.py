from django.contrib import admin

from .models import (
    Employee,
    ContinuousSequence,
    WeeklySum,
    PenalizedTransitions,
    WeeklyCoverDemand,
)


admin.site.register(Employee)
admin.site.register(ContinuousSequence)
admin.site.register(WeeklySum)
admin.site.register(PenalizedTransitions)
admin.site.register(WeeklyCoverDemand)


# TODO: add schedule and other models to make them show up in django admin
# admin.site.register(Schedule)
