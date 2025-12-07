from rest_framework import serializers
from app.models import Employee
import datetime

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = "__all__"

    #In REST we use validate instead of clean for validation
    def validate_salary(self, value):
        if value <= 0:
            raise serializers.ValidationError("Salary cannot be zero or less than that.")
        return value

    def validate_phone(self, value):
        if len(str(value)) != 10:
            raise serializers.ValidationError("Enter mobile number properly (10 digits required).")
        return value

    def validate_bonus(self, value):
        if value <= 0:
            raise serializers.ValidationError("Bonus should be greater than zero.")
        return value

    def validate_hire_date(self, value):
        if value > datetime.date.today():
            raise serializers.ValidationError("Hire date cannot be in the future.")
        return value
    
    def validate(self, data):
        if data['bonus'] > data['salary']:
            raise serializers.ValidationError("Bonus cannot be greater than salary.")
        return data
