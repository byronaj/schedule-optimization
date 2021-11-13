from rest_framework import serializers

from .models import (
    Employee,
    ContinuousSequence,
    WeeklySum,
    PenalizedTransitions,
    WeeklyCoverDemand,
)


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee

        read_only_fields = (
            'created',
        )

        fields = (
            'id',
            'first_name',
            'last_name',
            'fte',
            'shift_block',
            'is_active',
        )


class EmployeeShiftsSerializer(serializers.Serializer):
    # add fields to create an instance of an employee's schedule
    # this should result in one dict of all the shifts for an employee
    pass


class EmployeeScheduleSerializer(serializers.Serializer):
    employee = EmployeeShiftsSerializer(many=True)

    schedule_start_date = serializers.DateField()
    schedule_end_date = serializers.DateField()


class ContinuousSequenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContinuousSequence
        fields = '__all__'


class WeeklySumSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklySum
        fields = '__all__'


class PenalizedTransitionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PenalizedTransitions
        fields = '__all__'


class WeeklyCoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyCoverDemand
        fields = '__all__'
