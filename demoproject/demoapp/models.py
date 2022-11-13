from django.db import models
from django.contrib.auth.models import User
# Create your models here.
DESIGNATION_CHOICES =(
    ("DV", "Developer"),
    ("JD", "Junior Developer"),
    ("TL", "Team Lead"),
    ("MG", "Manager"),
)
class EmployeeDetails(models.Model):
    # pk_id = models.CharField(max_length=100, primary_key=True)
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    salary = models.FloatField(default=10000)
    image = models.ImageField(upload_to="employee_image", null=True, blank=True,
                        default="static/employee_image/profile_image.jpg")
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name_plural = "Employee Details"

class Profile(models.Model):
    username = models.OneToOneField(User, max_length=100, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, null=True, blank=True)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.firstname
    
    class Meta:
        verbose_name_plural = "Profiles"

class InsuaranceDetails(models.Model):
    full_name = models.ForeignKey(EmployeeDetails, on_delete=models.CASCADE)
    policy_name = models.CharField(max_length=50)
    policy_number = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Insurance Details"