from django.db import models
from django.core.validators import EmailValidator
from django.contrib.auth.models import User
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_profile')
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    photo = models.ImageField(upload_to='Images', null=True, blank=True)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE, default="Free")
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    Designation = models.ForeignKey(Role, on_delete=models.CASCADE) 
    phone = models.BigIntegerField()
    hire_date = models.DateField()
    email = models.EmailField(max_length=50, validators=[EmailValidator], null=False)

    def __str__(self):
        return  "%s %s" %(self.first_name, self.last_name)