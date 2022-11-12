from django.shortcuts import render, redirect
from django.http import JsonResponse, response
from demoapp.models import EmployeeDetails,InsuaranceDetails
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from .serializers import EmployeeDetailsSerializer
from rest_framework.response import Response
from django.core import serializers
import json

# Create your views here.
def index(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        age = request.POST.get('age')
        designation = request.POST.get('designation')
        salary = request.POST.get('salary')
        department = request.POST.get('department')
        
        try:
            employee_Detail = EmployeeDetails()
            employee_Detail.full_name = full_name
            employee_Detail.age = age
            employee_Detail.department = department
            employee_Detail.salary = salary
            employee_Detail.designation = designation
            employee_Detail.save()

        except Exception as e:
            print(e)
    return render(request,"index.html")


def policy(request):
    if request.method == "POST":
        policy_name = request.POST.get('policy_name')
        policy_number = request.POST.get('policy_number')

        full_name = request.POST.get('full_name')
        age = request.POST.get('age')
        designation = request.POST.get('designation')
        salary = request.POST.get('salary')
        department = request.POST.get('department')

        try:
            employee_Detail = EmployeeDetails()
            employee_Detail.full_name = full_name
            employee_Detail.age = age
            employee_Detail.department = department
            employee_Detail.salary = salary
            employee_Detail.designation = designation
            employee_Detail.save()
            
            employeePolicyDetail = InsuaranceDetails()
            employeePolicyDetail.full_name = employee_Detail
            employeePolicyDetail.policy_name = policy_name
            employeePolicyDetail.policy_number = policy_number
            employeePolicyDetail.save()

        except Exception as e:
            print(e)
    return render(request,"policy.html")

@csrf_exempt
def display_employees(request):
    employee_detail = EmployeeDetails.objects.all()
    print(len(employee_detail))
    serializer = serializers.serialize('json', employee_detail)
    context = {"employee_detail": employee_detail}
    # return render(request, "employee_details.html", context)
    return JsonResponse(json.loads(serializer), safe=False)

def delete_employees(request, id):
    try:
        print("id", id)
        EmployeeDetails.objects.filter(id=id).delete()
        return redirect('display_employees')
    except Exception as e:
        return JsonResponse({"Failure": "Something went wrong"}, safe=False)

def update_employee(request, id):
    if request.method == "POST":
        EmployeeDetails.objects.filter(id=id) \
                        .update(full_name=request.POST.get('full_name'))
    return redirect('display_employees')

@csrf_exempt
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        
        user_exist = User.objects.filter(username=username).first()
        if user_exist:
            
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user_exist)
                return JsonResponse({"Success": "Logged in"})
            else:
                return JsonResponse({"Success": "Password doesnt match"})
        else:
            return JsonResponse({"Success": "User doesnt exist"})
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('display_employees')


class EmployeeDetailsViewset(viewsets.ViewSet):
    queryset = EmployeeDetails.objects.all()
    serializer_class = EmployeeDetailsSerializer

    def list(self, request):
        print("Inside list method")
        get_all_employee = EmployeeDetails.objects.all()
        data = EmployeeDetailsSerializer(get_all_employee,many=True)
        return Response({'data': data.data}, content_type = 'application/json' )
    
    def destroy(self, request, id):
        print("inside destroy method")
        user_name = EmployeeDetails.objects.filter(id=id)
        user_name = user_name.full_name
        EmployeeDetails.objects.filter(id=id).delete()
        return Response({'data':f" {user_name} user is deleted"}, 
                        content_type = 'application/json' )