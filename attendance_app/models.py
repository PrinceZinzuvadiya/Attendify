from django.db import models
from datetime import datetime

class employee_attendance_details(models.Model):
    Inserted = models.DateTimeField(auto_now_add = True)
    Employee_id = models.IntegerField()
    First_name = models.CharField(max_length = 50)
    Last_name = models.CharField(max_length = 50)
    Job_role = models.CharField(max_length = 50)
    Department = models.CharField(max_length = 50)

class employee_leave_details(models.Model):
    Inserted = models.DateTimeField(auto_now_add = True)
    Employee_id = models.IntegerField()
    First_name = models.CharField(max_length = 50)
    Last_name = models.CharField(max_length = 50)
    Job_role = models.CharField(max_length = 50)
    Department = models.CharField(max_length = 50)
    From = models.CharField(max_length = 50)
    To = models.CharField(max_length = 50)
    Reason = models.CharField(max_length = 500)

class employee_details(models.Model):
    Employee_id = models.IntegerField()
    First_name = models.CharField(max_length = 50)
    Last_name = models.CharField(max_length = 50)
    Job_role = models.CharField(max_length = 50)
    Department = models.CharField(max_length = 50)
    last_insertion_time = models.DateTimeField(default=datetime.now)
