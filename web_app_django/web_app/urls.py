from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import EmployeeViewSet, GlobalConstraintsViewSet

router = DefaultRouter()
router.register('employees', EmployeeViewSet, basename='employees')
# router.register('globalconstraints', GlobalConstraintsViewSet, basename='globalconstraints')

urlpatterns = [
    path('', include(router.urls)),
]
