from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    # Fraction of hours this employee works compared to a full-time employee
    # E.g., 1.0 FTE = 1.0 * 40 = 40 hrs/week, 0.9 FTE = 40 * 0.9 = 36 hrs/week
    fte = models.DecimalField(max_digits=2, decimal_places=1, default=1.0)

    # Number indicating which shift (if any) an employee should be scheduled on
    # 0 = any, 1 = day shift, 2 = second shift, 3 = third shift
    shift_block = models.IntegerField(default=0)

    # To support the option of excluding certain employees from the schedule
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


# TODO: The employee model already has the needed fields for a MVP covered. Finish this to provide a way to store
#  employee requests for/against specific shifts
class EmployeeShiftPreference(models.Model):
    """Preference: (employee, shift, day, weight)
    Will need to auto-populate the 'requests' parameter of the scheduler with these values for every day in the schedule
    For employees with shift preference (Employee.shift_block != 0), the scheduler will use the shift preference
    """
    class Shifts(models.IntegerChoices):
        OFF = 0
        DAY = 1
        SECOND = 2
        NIGHT = 3

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    preferred_shift = models.IntegerField(choices=Shifts.choices)
    # day = all the days in the schedule
    # weight = repeat -2 for every day in the schedule


class ContinuousSequence(models.Model):
    """Shift constraints on a continuous sequence.
    E.g., (One or two consecutive days of rest), (Between 2 and 3 consecutive days of night shifts)
    shift_constraints = [(shift, hard_min, soft_min, min_penalty, soft_max, hard_max, max_penalty), (...)]
    """
    class Shifts(models.IntegerChoices):
        OFF = 0
        DAY = 1
        SECOND = 2
        NIGHT = 3

    shift_id = models.IntegerField(choices=Shifts.choices, default=Shifts.OFF)
    hard_min = models.IntegerField(default=0)
    soft_min = models.IntegerField(default=0)
    min_penalty = models.IntegerField(default=0)
    soft_max = models.IntegerField(default=0)
    hard_max = models.IntegerField(default=0)
    max_penalty = models.IntegerField(default=0)


class WeeklySum(models.Model):
    """Weekly sum constraints on shifts days:
    E.g., (Constraints on rests per week), (At least 1 night shift per week (penalized). At most 4 (hard))
    weekly_sum_constraints = [(shift, day, hard_min, soft_min, min_penalty, soft_max, hard_max, max_penalty), (...)]
    """
    class Shifts(models.IntegerChoices):
        OFF = 0
        DAY = 1
        SECOND = 2
        NIGHT = 3

    shift_id = models.IntegerField(choices=Shifts.choices, default=Shifts.OFF)
    hard_min = models.IntegerField(default=0)
    soft_min = models.IntegerField(default=0)
    min_penalty = models.IntegerField(default=0)
    soft_max = models.IntegerField(default=0)
    hard_max = models.IntegerField(default=0)
    max_penalty = models.IntegerField(default=0)


class PenalizedTransitions(models.Model):
    """Penalized transitions (0 means forbidden):
    E.g., (Afternoon to night has a penalty of 4), (Night to morning is forbidden)
    penalized_transitions = [(previous_shift, next_shift, penalty), (...)]
    """
    class Shifts(models.IntegerChoices):
        OFF = 0
        DAY = 1
        SECOND = 2
        NIGHT = 3

    previous_shift = models.IntegerField(choices=Shifts.choices, default=Shifts.OFF)
    next_shift = models.IntegerField(choices=Shifts.choices, default=Shifts.OFF)
    penalty = models.IntegerField(default=0)


class WeeklyCoverDemand(models.Model):
    """Daily demands for work shifts (morning, afternoon, night) for each day of the week, starting on Monday
    weekly_cover_demands = [mon: (morning, afternoon, night), tue: (morning, afternoon, night), ]
    """
    mon_shift1 = models.IntegerField(default=1)
    mon_shift2 = models.IntegerField(default=1)
    mon_shift3 = models.IntegerField(default=1)
    tue_shift1 = models.IntegerField(default=1)
    tue_shift2 = models.IntegerField(default=1)
    tue_shift3 = models.IntegerField(default=1)
    wed_shift1 = models.IntegerField(default=1)
    wed_shift2 = models.IntegerField(default=1)
    wed_shift3 = models.IntegerField(default=1)
    thu_shift1 = models.IntegerField(default=1)
    thu_shift2 = models.IntegerField(default=1)
    thu_shift3 = models.IntegerField(default=1)
    fri_shift1 = models.IntegerField(default=1)
    fri_shift2 = models.IntegerField(default=1)
    fri_shift3 = models.IntegerField(default=1)
    sat_shift1 = models.IntegerField(default=1)
    sat_shift2 = models.IntegerField(default=1)
    sat_shift3 = models.IntegerField(default=1)
    sun_shift1 = models.IntegerField(default=1)
    sun_shift2 = models.IntegerField(default=1)
    sun_shift3 = models.IntegerField(default=1)


class EmployeeSchedule(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    # TODO: link to the employee model
    # employee = models.ForeignKey('web_app.Employee', on_delete=models.CASCADE)

    employee = models.IntegerField(default=0)


class ShiftAssignment(models.Model):
    employee_schedule = models.ForeignKey(
        'EmployeeSchedule',
        related_name='shift_assignments',
        on_delete=models.CASCADE
    )
    shift_date = models.DateField()
    assignment = models.IntegerField(default=0)
