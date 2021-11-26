from django.contrib.auth.models import User

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    EmployeeSerializer,
    ContinuousSequenceSerializer,
    WeeklySumSerializer,
    PenalizedTransitionsSerializer,
    WeeklyCoverSerializer,
    EmployeeScheduleSerializer,
    ShiftAssignmentSerializer,
)
from .models import (
    Employee,
    ContinuousSequence,
    WeeklySum,
    PenalizedTransitions,
    WeeklyCoverDemand,
    EmployeeSchedule,
    ShiftAssignment,
)

from . import solver


class ScheduleSolverAPIView(APIView):
    """
    API endpoint view for initializing the solver and sending a response that contains the resulting generated schedule.
    """
    def get(self, request, *args, **kwargs):

        def serializer_to_tuple_list(serializer_object):
            """
            Converts a serializer object to a list of dictionaries, then converts that to a sequence of iterables.
            Trims off index 0 of each iterable, which is the id field.
            """
            constraints = serializer_object.data
            return [tuple(tuple(constraint.values())[1:]) for constraint in constraints]

        num_employees = Employee.objects.count()
        num_weeks = 3  # TODO: address this later
        shifts = ['0', '1', '2', '3']

        cs_constraint_serializer = ContinuousSequenceSerializer(ContinuousSequence.objects.all(), many=True)
        cs_constraint_list = serializer_to_tuple_list(cs_constraint_serializer)

        ws_constraint_serializer = WeeklySumSerializer(WeeklySum.objects.all(), many=True)
        ws_constraint_list = serializer_to_tuple_list(ws_constraint_serializer)

        pt_constraint_serializer = PenalizedTransitionsSerializer(PenalizedTransitions.objects.all(), many=True)
        pt_constraint_list = serializer_to_tuple_list(pt_constraint_serializer)

        coverage_serializer = WeeklyCoverSerializer(WeeklyCoverDemand.objects.all(), many=True)

        # returns one dict of coverage demands for three shifts per day, from Monday to Sunday
        coverage = coverage_serializer.data

        # trim off pk and convert to a list of tuples of shifts for each day
        coverage_tuple = tuple(coverage[0].values())[1:]
        weekly_cover_demands = [tuple(coverage_tuple[i:i + 3]) for i in range(0, len(coverage_tuple), 3)]

        result = solver.solve_shift_scheduling(
            num_employees,
            num_weeks,
            shifts,
            cs_constraint_list,
            ws_constraint_list,
            pt_constraint_list,
            weekly_cover_demands
        )

        # TODO: this does work for saving the schedule, but it needs to do so only for employees without a pre-existing
        #  schedule and simply update the records otherwise
        # for employee_schedule in result:
        #     try:
        #         es_serializer = EmployeeScheduleSerializer(data=employee_schedule)
        #         if es_serializer.is_valid():
        #             es_serializer.save()
        #             print('employee schedule validated and saved successfully')
        #     except Exception as e:
        #         print(e)

        response = Response(result, status=status.HTTP_200_OK)
        return response


class EmployeeScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeScheduleSerializer
    queryset = EmployeeSchedule.objects.all()


class ShiftAssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = ShiftAssignmentSerializer
    queryset = ShiftAssignment.objects.all()


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #
    #     return Response(serializer.data)


class ContinuousSequenceViewSet(viewsets.ModelViewSet):
    serializer_class = ContinuousSequenceSerializer
    queryset = ContinuousSequence.objects.all()


class WeeklySumViewSet(viewsets.ModelViewSet):
    serializer_class = WeeklySumSerializer
    queryset = WeeklySum.objects.all()


class PenalizedTransitionsViewSet(viewsets.ModelViewSet):
    serializer_class = PenalizedTransitionsSerializer
    queryset = PenalizedTransitions.objects.all()


class WeeklyCoverViewSet(viewsets.ModelViewSet):
    serializer_class = WeeklyCoverSerializer
    queryset = WeeklyCoverDemand.objects.all()


# A fine work of art courtesy of GitHub Copilot
# def get_garbage...
def get_garbage_employees(request):
    """
    Returns a list of employees that are garbage.
    """
    employees = Employee.objects.filter(is_garbage=True)
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)
