from django import forms
from .models import Role, Employee, Department

import datetime

class Employee_form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)  # to remove logged-in user
        super().__init__(*args, **kwargs)

        designation = ""  

        if user:
            # Check if user has an Employee profile
            if hasattr(user, "employee_profile") and user.employee_profile:
                if user.employee_profile.Designation:  # check if Designation exists
                    designation = user.employee_profile.Designation.name

        # Hide salary & bonus if not Manager or no designation
        if designation != "Manager":
            self.fields.pop("salary", None)
            self.fields.pop("bonus", None)

                
   
    class Meta:
        model = Employee
        exclude = ['user'] 
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder':"ex. Ajay", 'class':'form-control','required': 'required' }),
            'last_name': forms.TextInput(attrs={'placeholder':"ex. Kohli",'class':'form-control', 'required': 'required'}),
            'photo': forms.FileInput(attrs={'class':'form-control', 'type':'file','required': 'required'}),
            'department': forms.Select(attrs={"class":"form-select",'required': 'required'}),
            'salary': forms.NumberInput(attrs={'placeholder':"ex. 10,000",'class':'form-control', }),
            'bonus': forms.NumberInput(attrs={'placeholder':"ex. 1,000",'class':'form-control', }),
            'designation': forms.Select(attrs={ "class":"form-select", 'required': 'required' }),
            'phone': forms.NumberInput(attrs={'class':'form-control', 'required': 'required'}),
            'hire_date': forms.DateInput(attrs={'class':'form-control', 'type':'date', 'required': 'required'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'type':'email', 'required': 'required'}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phone': 'Mobile Number',
        }
    
    # ✔ Validation for salary
    def clean_salary(self):
        if "salary" not in self.cleaned_data:
            return self.instance.salary  # return original value for non-managers
        salary = self.cleaned_data.get('salary')
        if salary <= 0:
            raise forms.ValidationError("Salary cannot be zero or less than that.")
        return salary

    def clean_bonus(self):
        if "bonus" not in self.cleaned_data:
            return self.instance.bonus  # return original value for non-managers
        bonus = self.cleaned_data.get('bonus')
        if bonus <= 0:
            raise forms.ValidationError("Bonus should be greater than zero.")
        return bonus

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if len(str(phone)) != 10:
            raise forms.ValidationError("Enter mobile number properly")

        return phone

    # Validation for hire date (no future date)
    def clean_hire_date(self):
        hire_date = self.cleaned_data.get('hire_date')

        if hire_date > datetime.date.today():
            raise forms.ValidationError("Hire date cannot be in the future.")

        return hire_date