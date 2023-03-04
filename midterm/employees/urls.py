from django.urls import path
from employees import views

urlpatterns = [
    path('employees', views.employees_handler),
    path('employees/<int:pk>', views.employee_handler),
]