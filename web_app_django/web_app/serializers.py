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


# not currently implemented
class ShiftAssignments:
    def __init__(self, json_data):
        # self.employee = employee
        self.json_data = json_data


# not currently implemented
class ShiftAssignmentsSerializer(serializers.Serializer):
    # add fields to create an instance of an employee's schedule
    # this should result in one dict of all the shifts for an employee
    # employee = EmployeeSerializer(many=True)
    shifts = serializers.ListField()

    def create(self, validated_data):
        return ShiftAssignments(**validated_data)

    def update(self, instance, validated_data):
        # instance.employee = validated_data.get('employee', instance.employee)
        instance.shifts = validated_data.get('shifts', instance.shifts)


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
