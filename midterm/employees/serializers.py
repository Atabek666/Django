from rest_framework import serializers
from employees.models import Employee


class EmployeesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    full_name = serializers.CharField(min_length=5, max_length=50, allow_null=False)
    position = serializers.CharField(allow_null=False, allow_blank=False)
    salary = serializers.IntegerField(min_value=0, max_value=10000000, allow_null=False)

    def create(self, validated_data):
        employee = Employee(**validated_data)
        employee.save()
        return employee

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('name', instance.full_name)
        instance.save()
        return instance
