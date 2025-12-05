from django import forms
from .models import Role, Employee, Department

import datetime

class Employee_form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder':"ex. Ajay", 'class':'form-control','required': 'required' }),
            'last_name': forms.TextInput(attrs={'placeholder':"ex. Kohli",'class':'form-control', 'required': 'required'}),
            'department': forms.Select(attrs={"class":"custom-select custom-select-lg",'required': 'required'}),
            'salary': forms.NumberInput(attrs={'placeholder':"ex. 10,000",'class':'form-control', 'required': 'required'}),
            'bonus': forms.NumberInput(attrs={'placeholder':"ex. 1,000",'class':'form-control', 'required': 'required'}),
            'designation': forms.Select(attrs={ "class":"custom-select custom-select-lg", 'required': 'required' }),
            'phone': forms.NumberInput(attrs={'class':'form-control', 'required': 'required'}),
            'hire_date': forms.DateInput(attrs={'class':'form-control', 'type':'date', 'required': 'required'}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phone': 'Mobile Number',
        }
    
    # ✔ Validation for salary
    def clean_salary(self):
        salary = self.cleaned_data.get('salary')

        if salary <= 0:
            raise forms.ValidationError("Salary cannot be zero or less than that.")

        return salary
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if len(str(phone)) != 10:
            raise forms.ValidationError("Enter mobile number properly")

        return phone

    # ✔ Validation for bonus
    def clean_bonus(self):
        bonus = self.cleaned_data.get('bonus')

        if bonus <= 0:
            raise forms.ValidationError("Bonus should be greater than zero.")

        return bonus

    # ✔ Validation for hire date (no future date)
    def clean_hire_date(self):
        hire_date = self.cleaned_data.get('hire_date')

        if hire_date > datetime.date.today():
            raise forms.ValidationError("Hire date cannot be in the future.")

        return hire_date