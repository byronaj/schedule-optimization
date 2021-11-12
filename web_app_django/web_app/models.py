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


# Is this really even needed? The employee model already has the needed fields covered.
# The only use this would have is to provide a way to store employee requests for/against specific shifts
class EmployeeShiftPreference(models.Model):
    """Preference: (employee, shift, day, weight)
    Will need to auto-populate the 'requests' parameter of the scheduler with these values for every day in the schedule
    For employees with shift preference (Employee.shift_block != 0), the scheduler will use the shift preference
    """
    SHIFTS = (
        (0, 'Off'),
        (1, 'Day'),
        (2, 'Second'),
        (3, 'Third'),
    )

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    preferred_shift = models.IntegerField(choices=SHIFTS)
    # day = all the days in the schedule
    # weight = repeat -2 for every day in the schedule


class ContinuousSequence(models.Model):
    """Shift constraints on a continuous sequence.
    E.g., (One or two consecutive days of rest), (Between 2 and 3 consecutive days of night shifts)
    shift_constraints = [(shift, hard_min, soft_min, min_penalty, soft_max, hard_max, max_penalty), (...)]
    """
    SHIFTS = (
        (0, 'Off'),
        (1, 'Day'),
        (2, 'Second'),
        (3, 'Third'),
    )

    shift_id = models.IntegerField(choices=SHIFTS, default=0)
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
    SHIFTS = (
        (0, 'Off'),
        (1, 'Day'),
        (2, 'Second'),
        (3, 'Third'),
    )

    shift_id = models.IntegerField(choices=SHIFTS, default=0)
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
    SHIFTS = (
        (0, 'Off'),
        (1, 'Day'),
        (2, 'Second'),
        (3, 'Third'),
    )

    previous_shift = models.IntegerField(choices=SHIFTS, default=0)
    next_shift = models.IntegerField(choices=SHIFTS, default=0)
    penalty = models.IntegerField(default=0)


class DailyCoverDemands(models.Model):
    num_shift_1 = models.IntegerField(default=0)
    num_shift_2 = models.IntegerField(default=0)
    num_shift_3 = models.IntegerField(default=0)


class WeeklyCoverDemands(models.Model):
    """Daily demands for work shifts (morning, afternoon, night) for each day of the week, starting on Monday
    weekly_cover_demands = [mon: (morning, afternoon, night), tue: (morning, afternoon, night), etc.]
    """
    day_0 = models.ForeignKey(DailyCoverDemands, on_delete=models.CASCADE, related_name='monday')
    day_1 = models.ForeignKey(DailyCoverDemands, on_delete=models.CASCADE, related_name='tuesday')
    day_2 = models.ForeignKey(DailyCoverDemands, on_delete=models.CASCADE, related_name='wednesday')
    day_3 = models.ForeignKey(DailyCoverDemands, on_delete=models.CASCADE, related_name='thursday')
    day_4 = models.ForeignKey(DailyCoverDemands, on_delete=models.CASCADE, related_name='friday')
    day_5 = models.ForeignKey(DailyCoverDemands, on_delete=models.CASCADE, related_name='saturday')
    day_6 = models.ForeignKey(DailyCoverDemands, on_delete=models.CASCADE, related_name='sunday')


# class Schedule(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     is_active = models.BooleanField(default=True)
#
#     # List of employees that are scheduled to work on this schedule
#     employees = models.ManyToManyField(Employee)
#
#     # List of constraints that apply to this schedule
#     constraints = models.ManyToManyField(EmployeeConstraints)
#
#     # List of shifts that apply to this schedule
#     shifts = models.ManyToManyField('Shift')
#
#     def __str__(self):
#         return "Schedule " + str(self.id) + ": " + str(self.start_date) + " - " + str(self.end_date)
