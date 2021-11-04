from django.contrib.auth.models import User

from rest_framework import viewsets

from .serializers import EmployeeSerializer, GlobalConstraintsSerializer
# from .serializers import UserSerializer

from .models import Employee, GlobalConstraints


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset.filter()

    def perform_update(self, serializer):
        serializer.save()


class GlobalConstraintsViewSet(viewsets.ModelViewSet):
    serializer_class = GlobalConstraintsSerializer
    queryset = GlobalConstraints.objects.all()

    def get_queryset(self):
        return self.queryset.filter()

    def perform_update(self, serializer):
        serializer.save()
