from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    EmployeeViewSet,
    ContinuousSequenceViewSet,
    WeeklySumViewSet,
    PenalizedTransitionsViewSet,
    WeeklyCoverViewSet,
    EmployeeScheduleViewSet,
    ShiftAssignmentViewSet,
    ScheduleSolverAPIView,
)


router = DefaultRouter()
router.register('employees', EmployeeViewSet, basename='employees')
router.register('sequences', ContinuousSequenceViewSet, basename='sequences')
router.register('weeklysums', WeeklySumViewSet, basename='weeklysums')
router.register('transitions', PenalizedTransitionsViewSet, basename='transitions')
router.register('coverages', WeeklyCoverViewSet, basename='coverages')
router.register('schedule', EmployeeScheduleViewSet, basename='schedule')
router.register('shifts', ShiftAssignmentViewSet, basename='shifts')

urlpatterns = [
    path('', include(router.urls)),
    path('schedulesolver/', ScheduleSolverAPIView.as_view(), name='schedulesolver'),
]
