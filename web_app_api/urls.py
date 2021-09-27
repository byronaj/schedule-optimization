from django.urls import path
from .views import EmployeeList, EmployeeDetail

app_name = 'web_app_api'

urlpatterns = [
    path('<int:pk>/', EmployeeDetail.as_view(), name='detailcreate'),
    path('', EmployeeList.as_view(), name='listcreate'),
]
