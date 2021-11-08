from rest_framework import serializers

from .models import Employee, ContinuousSequenceConstraint, WeeklySumConstraint, PenalizedTransitionsConstraint


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
        model = ContinuousSequenceConstraint

        fields = (
            'id',
            'shift_id',
            'hard_min',
            'soft_min',
            'min_penalty',
            'soft_max',
            'hard_max',
            'max_penalty',
        )


class WeeklySumSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklySumConstraint

        fields = (
            'id',
            'shift_id',
            'hard_min',
            'soft_min',
            'min_penalty',
            'soft_max',
            'hard_max',
            'max_penalty',
        )


class PenalizedTransitionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PenalizedTransitionsConstraint

        fields = (
            'id',
            'previous_shift',
            'next_shift',
            'penalty',
            )


# TODO: serialize daily coverage
