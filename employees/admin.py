from django.contrib import admin
from .models import Employee, Salary

# Register your models here.
class SalaryInline(admin.StackedInline):
    model = Salary

class EmployeeAdmin(admin.ModelAdmin):
    inlines = [
        SalaryInline,
    ]

admin.site.register(Employee, EmployeeAdmin)