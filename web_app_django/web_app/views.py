from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    EmployeeSerializer,
    ContinuousSequenceSerializer,
    WeeklySumSerializer,
    PenalizedTransitionsSerializer,
    EmployeeShiftsSerializer,
)
from .models import (
    Employee,
    ContinuousSequence,
    WeeklySum,
    PenalizedTransitions,
    WeeklyCoverDemands,
)

from . import solver


class ReportView(APIView):
    """
    API endpoint view for initializing the solver and sending a response that contains the resulting generated schedule.
    """

    def get(self, request, *args, **kwargs):

        # Leaving this here for now, but it's not used.
        # Serialize employee objects into a list of dictionaries
        employee_serializer = EmployeeSerializer(Employee.objects.all(), many=True)
        employee_list = employee_serializer.data
        # [
        #     {'id': 0, 'first_name': 'first0', 'last_name': 'last0', 'fte': 0.0, 'shift_block': 0, 'is_active': True},
        #     {'id': 1, 'first_name': 'first1', 'last_name': 'last1', 'fte': 0.0, 'shift_block': 0, 'is_active': True},
        #     {'id': 2, 'first_name': 'first2', 'last_name': 'last2', 'fte': 0.0, 'shift_block': 0, 'is_active': True}
        # ]

        def serializer_to_tuple_list(serializer_object):
            """
            Converts a serializer object to a list of dictionaries, then converts that to a list of tuples.
            """
            constraints = serializer_object.data
            return [tuple(constraint.values()) for constraint in constraints]

        num_employees = Employee.objects.count()
        num_weeks = 3  # TODO: address this later
        shifts = ['O', 'M', 'A', 'N']  # TODO: this is 'tarded, but w/e, address later

        cs_constraint_serializer = ContinuousSequenceSerializer(ContinuousSequence.objects.all(), many=True)
        cs_constraint_list = serializer_to_tuple_list(cs_constraint_serializer)

        ws_constraint_serializer = WeeklySumSerializer(WeeklySum.objects.all(), many=True)
        ws_constraint_list = serializer_to_tuple_list(ws_constraint_serializer)

        pt_constraint_serializer = PenalizedTransitionsSerializer(PenalizedTransitions.objects.all(), many=True)
        pt_constraint_list = serializer_to_tuple_list(pt_constraint_serializer)

        result = solver.solve_shift_scheduling(
            num_employees,
            num_weeks,
            shifts,
            cs_constraint_list,
            ws_constraint_list,
            pt_constraint_list,
        )

        # Have the generated schedule formatted to be sent back as a response
        serializer = EmployeeShiftsSerializer(result, many=True)

        return Response(serializer.data)


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #
    #     return Response(serializer.data)


# A fine work of art courtesy of GitHub Copilot
def get_garbage_employees(request):
    """
    Returns a list of employees that are garbage.
    """
    employees = Employee.objects.filter(is_garbage=True)
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)
