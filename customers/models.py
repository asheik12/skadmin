from django.db import models
from skadmin.validators import validate_phone
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=55, blank=True, null=True)
    address = models.CharField(max_length=55, blank=True, null=True)
    mobile = models.CharField(max_length=10, unique=True, validators=[validate_phone])
    email = models.EmailField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name