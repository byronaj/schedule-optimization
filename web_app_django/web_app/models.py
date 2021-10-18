from django.contrib.auth.models import User
from django.db import models
# from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     pass


class Employee(models.Model):

    class EmployeeObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='active')

    name = models.CharField(max_length=100)

    # Number indicating which shift (if any) an employee should be scheduled on
    # 0 = any, 1 = day shift, 2 = night shift
    shift = models.IntegerField()

    # Fraction of hours this employee works compared to a full-time employee
    # E.g., 1.0 FTE = 1.0 * 40 = 40 hrs/week, 0.9 FTE = 40 * 0.9 = 36 hrs/week
    fte = models.FloatField()
    active = models.BooleanField(default=True)
    objects = models.Manager()
    employee_objects = EmployeeObjects()
