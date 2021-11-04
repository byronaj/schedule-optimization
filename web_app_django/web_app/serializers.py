from rest_framework import serializers

from .models import Employee, GlobalConstraints


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


class GlobalConstraintsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalConstraints

        fields = (
            'id',
            'shift',
            'shift_hard_min',
            'shift_soft_min',
            'shift_min_penalty',
            'shift_soft_max',
            'shift_hard_max',
            'shift_max_penalty',
            'weekly_sum_shift',
            'weekly_sum_hard_min',
            'weekly_sum_soft_min',
            'weekly_sum_min_penalty',
            'weekly_sum_soft_max',
            'weekly_sum_hard_max',
            'weekly_sum_max_penalty',
            'previous_shift',
            'next_shift',
            'penalty',
        )
