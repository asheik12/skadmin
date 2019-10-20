from django.db import models
from customers.models import Customer
# Create your models here.

class SType(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    total_amount = models.DecimalField(max_digits=7, decimal_places=2)
    remarks = models.TextField(max_length=500, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.first_name

class Service(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    stype = models.ForeignKey(SType, on_delete=models.DO_NOTHING)
    no = models.PositiveSmallIntegerField(default=1)
    amount =  models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.stype.name
  