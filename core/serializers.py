from rest_framework import serializers

from core.models import Position, Salary, Employee


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    position = PositionSerializer()
    get_all_salary = serializers.FloatField()
    salary = SalarySerializer(many=True)

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'patronymic', 'position', 'employment_date', 'chief',
                  'wages', 'get_all_salary', 'salary']


