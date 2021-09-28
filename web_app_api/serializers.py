from rest_framework import serializers
from web_app.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name', 'shift', 'fte', 'active')
        # fields = '__all__'
