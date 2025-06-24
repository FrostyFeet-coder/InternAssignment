from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Manager, Employee
from .serializers import ManagerSerializer, EmployeeSerializer

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        manager_id = str(instance.id)
        manager_name = instance.name
        self.perform_destroy(instance)
        return Response(
            {
                "message": f"Manager '{manager_name}' with ID {manager_id} has been deleted."
            },
            status=status.HTTP_200_OK
        )

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        employee_id = str(instance.id)
        employee_name = instance.name
        self.perform_destroy(instance)
        return Response(
            {
                "message": f"Employee '{employee_name}' with ID {employee_id} has been deleted."
            },
            status=status.HTTP_200_OK
        )

    @action(detail=False, methods=['get'], url_path='by-manager/(?P<manager_id>[0-9a-f-]+)')
    def get_employees_by_manager(self, request, manager_id=None):
        employees = Employee.objects.filter(manager__id=manager_id)
        serializer = self.get_serializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
