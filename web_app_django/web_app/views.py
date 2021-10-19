from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.conf import settings
from django.shortcuts import render, redirect

from rest_framework import permissions
from rest_framework import serializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EmployeeDetail(generics.RetrieveDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# def index(request):
#     return render(request, 'index.html')


# @login_required
# def logout(request):
#     django_logout(request)
#     domain = settings.SOCIAL_AUTH_AUTH0_DOMAIN
#     client_id = settings.SOCIAL_AUTH_AUTH0_KEY
#     return_to = 'http://127.0.0.1:8000'  # this can be current domain
#     return redirect(f'https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}')
