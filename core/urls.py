from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ManagerViewSet, EmployeeViewSet

router = DefaultRouter()
router.register(r'managers', ManagerViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
