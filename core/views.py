from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Employee
from core.serializers import EmployeeSerializer


class EmployeeList(APIView):

    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        employees = Employee.objects.all().select_related('position').prefetch_related('salary_set')
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetail(APIView):

    permission_classes = [permissions.IsAdminUser]

    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeeListByPosition(APIView):

    permission_classes = [permissions.IsAdminUser]

    def get(self, request, level):
        employees = Employee.objects.filter(position__level=level)\
            .select_related('position').prefetch_related('salary_set')
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
