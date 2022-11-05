from django.shortcuts import render, redirect
from django.http import JsonResponse
from demoapp.models import EmployeeDetails,InsuaranceDetails

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

def display_employees(request):
    employee_detail = EmployeeDetails.objects.all()
    print(len(employee_detail))
    context = {"employee_detail": employee_detail}
    return render(request, "employee_details.html", context)

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
