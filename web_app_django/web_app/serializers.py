from rest_framework import serializers

from .models import Employee


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = (
#             "id",
#             "username",
#             "first_name",
#             "last_name",
#         )


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee

        fields = (
            'id',
            'first_name',
            'last_name',
            'fte',
            'shift_block',
            'is_active',
            # 'created_by',
            # 'created_at',
            # 'modified_at',
        )
