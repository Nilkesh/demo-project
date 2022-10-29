from django.db import models

# Create your models here.
DESIGNATION_CHOICES =(
    ("DV", "Developer"),
    ("JD", "Junior Developer"),
    ("TL", "Team Lead"),
    ("MG", "Manager"),
)
class EmployeeDetails(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.CharField(max_length=100)
    designation = models.CharField(choices=DESIGNATION_CHOICES, max_length=50)
    salary = models.FloatField(default=10000)
    
    def __str__(self):
        return self.full_name
    
    class meta:
        verbose_plurals = "Employee Details"

class InsuaranceDetails(models.Model):
    full_name = models.ForeignKey(EmployeeDetails, on_delete=models.CASCADE)
    policy_name = models.CharField(max_length=50)
    policy_number = models.CharField(max_length=50)