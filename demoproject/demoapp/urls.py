from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("router_employee_detail", views.EmployeeDetailsViewset, basename="router_employee")

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login_user_jwt/', views.login_user_jwt, name="login_user_jwt"),
    path('index/', views.index, name="index"),
    path('policy/', views.policy, name="policy"),
    path('display_employees/', views.display_employees, name="display_employees"),
    #deleting the employee
    path('delete_employees/<str:id>', views.delete_employees, name="delete_employees"),
    path('update_employee/<str:id>', views.update_employee, name="update_employees"),
    path('login_user/', views.login_user, name="login_user"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('employee_details/', views.EmployeeDetailsViewset.as_view({'get': 'list'}), name="employee_details"),
    path('employee_details/<str:id>', views.EmployeeDetailsViewset.as_view({'delete': 'destroy'}), name="individual_employee_update"),

]

urlpatterns += router.urls