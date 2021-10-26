from django.urls import path
from core import views

urlpatterns = [
    path('employee_create/', views.EmployeeList.as_view(), name='creater'),
    path('employee_detail/<int:pk>/', views.EmployeeDetail.as_view(), name='detail'),
    path('<str:level>/', views.EmployeeListByPosition.as_view(), name='position')
]