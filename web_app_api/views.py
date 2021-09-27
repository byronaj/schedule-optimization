from django.shortcuts import render
from rest_framework import generics
from web_app.models import Employee
from .serializers import EmployeeSerializer


# Create your views here.
class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(generics.RetrieveDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
