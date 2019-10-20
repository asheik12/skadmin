from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=55, blank=True, null=True)
    dob = models.DateField(verbose_name='Date of Birth')
    doj = models.DateField(verbose_name='Date of Joining')
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.first_name

class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=7, decimal_places=2)
    is_active = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee.first_name