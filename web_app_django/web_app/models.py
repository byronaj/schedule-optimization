from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    # Fraction of hours this employee works compared to a full-time employee
    # E.g., 1.0 FTE = 1.0 * 40 = 40 hrs/week, 0.9 FTE = 40 * 0.9 = 36 hrs/week
    fte = models.FloatField()

    # Number indicating which shift (if any) an employee should be scheduled on
    # 0 = any, 1 = day shift, 2 = night shift
    shift_block = models.IntegerField()

    is_active = models.BooleanField(default=True)

    # created_by = models.ForeignKey(User, related_name='employees', on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True)
    # modified_at = models.DateTimeField(auto_now=True)


# class GlobalConstraints(models.Model):
#
#     # Shift constraints on continuous sequence:
#     # shift_constraints = [shift, hard_min, soft_min, min_penalty, soft_max, hard_max, max_penalty]
#     shift = models.IntegerField(default=0)
#     shift_hard_min = models.IntegerField(default=0)
#     shift_soft_min = models.IntegerField(default=0)
#     shift_min_penalty = models.IntegerField(default=0)
#     shift_soft_max = models.IntegerField(default=0)
#     shift_hard_max = models.IntegerField(default=0)
#     shift_max_penalty = models.IntegerField(default=0)
#
#     # Weekly sum constraints on shifts days:
#     # weekly_sum_constraints = [shift, hard_min, soft_min, min_penalty, soft_max, hard_max, max_penalty]
#     weekly_sum_shift = models.IntegerField(default=0)
#     weekly_sum_hard_min = models.IntegerField(default=0)
#     weekly_sum_soft_min = models.IntegerField(default=0)
#     weekly_sum_min_penalty = models.IntegerField(default=0)
#     weekly_sum_soft_max = models.IntegerField(default=0)
#     weekly_sum_hard_max = models.IntegerField(default=0)
#     weekly_sum_max_penalty = models.IntegerField(default=0)
#
#     # Penalized transitions (0 means forbidden):
#     # penalized_transitions = [previous_shift, next_shift, penalty]
#     # finish later
#
#     # Daily demands for work shifts (morning, afternoon, night) for each day:
#     # weekly_cover_demands = [mon: (morning, afternoon, night), tue: (morning, afternoon, night), etc.]
#     # finish later
