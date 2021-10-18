from django.urls import path

from .views import EmployeeList, EmployeeDetail
# from web_app import views


urlpatterns = [
    # path('', views.index, name='index'),
    # path('logout/', views.logout, name='logout'),
    path('<int:pk>/', EmployeeDetail.as_view(), name='detailcreate'),
    path('', EmployeeList.as_view(), name='listcreate'),
]
