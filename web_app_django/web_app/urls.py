from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import EmployeeViewSet

router = DefaultRouter()
router.register('employees', EmployeeViewSet, basename='employees')

urlpatterns = [
    path('', include(router.urls)),
    # path('/report', ReportView.as_view(), name='report'),
]
