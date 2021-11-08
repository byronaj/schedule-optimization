from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import EmployeeSerializer, EmployeeShiftsSerializer
from .models import Employee

# from .schedule_information import ScheduleInformation
# from . import solver


class ReportView(APIView):
    """API endpoint for initializing the solver and sending a response containing the generated schedule.
    """

    def get(self, request, format=None):

        # employee_fte = {'fte': employee.fte for employee in Employee.objects.all()}

        # Serialize employee objects into a list of dictionaries
        employee_serializer = EmployeeSerializer(Employee.objects.all(), many=True)
        employee_dicts = employee_serializer.data
        # [
        #     {'id': 0, 'first_name': 'first0', 'last_name': 'last0', 'fte': 0.0, 'shift_block': 0, 'is_active': True},
        #     {'id': 1, 'first_name': 'first1', 'last_name': 'last1', 'fte': 0.0, 'shift_block': 0, 'is_active': True},
        #     {'id': 2, 'first_name': 'first2', 'last_name': 'last2', 'fte': 0.0, 'shift_block': 0, 'is_active': True}
        # ]

        # finish serializing objects and then manipulate to usable solver parameters

        num_employees = len(employee_dicts)
        num_weeks = 3  # TODO: address this later
        shifts = ['O', 'M', 'A', 'N']
        shift_constraints = [()]
        weekly_sum_constraints = [()]
        penalized_transitions = [()]

        # solver_parameters = ScheduleInformation(
        #     num_employees,
        #     num_weeks,
        #     shifts,
        #     shift_constraints,
        #     weekly_sum_constraints,
        #     penalized_transitions
        # )

        # solver.SI = solver_parameters
        # results = solver

        # Have the generated schedule formatted to be sent back as a response
        # serializer = EmployeeShiftsSerializer(results, many=True)

        # return Response(serializer.data)


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #
    #     return Response(serializer.data)


# class ScheduleViewSet(viewsets.ModelViewSet):
#     serializer_class = EmployeeSerializer
#     queryset = Employee.objects.all()


# A fine work of art courtesy of GitHub Copilot
def get_garbage_employees(request):
    """
    Returns a list of employees that are garbage.
    """
    employees = Employee.objects.filter(is_garbage=True)
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)
