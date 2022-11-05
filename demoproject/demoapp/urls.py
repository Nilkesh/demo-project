from django.urls import path, include
from . import views
urlpatterns = [
    path('index/', views.index, name="index"),
    path('policy/', views.policy, name="policy"),
    path('display_employees/', views.display_employees, name="display_employees"),
    #deleting the employee
    path('delete_employees/<str:id>', views.delete_employees, name="delete_employees"),
    path('update_employee/<str:id>', views.update_employee, name="update_employees"),

]