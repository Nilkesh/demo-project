from .models import EmployeeDetails, InsuaranceDetails
from rest_framework import routers, serializers, viewsets

class EmployeeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDetails
        # fields = '__all__'
        exclude = ('salary', )
        # fields = ['full_name', 'department']
