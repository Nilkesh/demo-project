from django.contrib import admin
from .models import InsuaranceDetails, EmployeeDetails, Profile
# Register your models here.
admin.site.register(InsuaranceDetails)
admin.site.register(EmployeeDetails)
admin.site.register(Profile)