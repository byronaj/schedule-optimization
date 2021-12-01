from rest_framework import serializers

from .models import (
    Employee,
    ContinuousSequence,
    WeeklySum,
    PenalizedTransitions,
    WeeklyCoverDemand,
    ShiftAssignment,
    EmployeeSchedule,
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


class ShiftAssignmentSerializer(serializers.ModelSerializer):

    # TODO: Added to make shift assignments identifiable and therefore updatable
    # id = serializers.IntegerField(required=False)

    class Meta:
        model = ShiftAssignment
        fields = ['shift_date', 'assignment']


class EmployeeScheduleSerializer(serializers.ModelSerializer):
    shift_assignments = ShiftAssignmentSerializer(many=True)

    class Meta:
        model = EmployeeSchedule
        fields = ['employee', 'shift_assignments']

    def create(self, validated_data):
        shifts_data = validated_data.pop('shift_assignments')
        employee_schedule = EmployeeSchedule.objects.create(**validated_data)

        for shift_data in shifts_data:
            ShiftAssignment.objects.create(employee_schedule=employee_schedule, **shift_data)

        return employee_schedule

    # TODO: Update is not fully implemented yet
    # def update(self, instance, validated_data):
    #     shifts_data = validated_data.pop('shift_assignments')
    #     shifts_data = instance.shift_assignments
    #     for shift_data in shifts_data:
    #         shift_data.shift_date = shift_data.shift_date
    #         shift_data.assignment = shift_data.assignment
    #         shift_data.save()
    #     return instance


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
