from django.db import models

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
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    photo = models.ImageField(upload_to='Images')
    Department = models.ForeignKey(Department, on_delete=models.CASCADE, default="Free")
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    Designation = models.ForeignKey(Role, on_delete=models.CASCADE) 
    phone = models.BigIntegerField()
    hire_date = models.DateField()

    def __str__(self):
        return  "%s %s" %(self.first_name, self.last_name)