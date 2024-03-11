from django.contrib import admin
from .models import *

class Attendance_model(admin.ModelAdmin):
    list_display = ['Inserted', 'Employee_id', 'First_name', 'Last_name', 'Job_role', 'Department']
admin.site.register(employee_attendance_details, Attendance_model)

class Leave_model(admin.ModelAdmin):
    list_display = ['Inserted', 'Employee_id', 'First_name', 'Last_name', 'Job_role', 'Department', 'Reason']
admin.site.register(employee_leave_details, Leave_model)

class Employee_model(admin.ModelAdmin):
    list_display = ['Employee_id', 'First_name', 'Last_name', 'Job_role', 'Department']
admin.site.register(employee_details, Employee_model)
