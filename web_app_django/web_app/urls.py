from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('employees', views.EmployeeViewSet, basename='employees')
router.register('sequences', views.ContinuousSequenceViewSet, basename='sequences')
router.register('weeklysums', views.WeeklySumViewSet, basename='weeklysums')
router.register('transitions', views.PenalizedTransitionsViewSet, basename='transitions')
router.register('coverages', views.WeeklyCoverViewSet, basename='coverages')

urlpatterns = [
    path('', include(router.urls)),
    path('report/', views.ReportView.as_view(), name='report'),
]
