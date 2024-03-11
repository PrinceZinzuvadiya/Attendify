from django import forms
from .models import employee_attendance_details, employee_leave_details

class attendance_form(forms.ModelForm):
    class Meta:
        model = employee_attendance_details
        fields = '__all__'

class leave_form(forms.ModelForm):
    class Meta:
        model = employee_leave_details
        fields = '__all__'

