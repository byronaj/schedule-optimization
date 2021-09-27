from rest_framework import serializers
from web_app.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'shift', 'fte', 'active')
        model = Employee
