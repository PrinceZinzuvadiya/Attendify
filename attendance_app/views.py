from django.shortcuts import render, redirect
from .forms import attendance_form, leave_form
from .models import employee_details
from django.contrib import messages
from datetime import datetime, timedelta
from django.core.mail import send_mail

def home(request):
    return render (request, 'homepage.html')

def attendance(request):
    if request.method == 'POST':
        form = attendance_form(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data['Employee_id']
            if employee_details.objects.filter(Employee_id=employee_id).exists():
                employee = employee_details.objects.get(Employee_id=employee_id)
                last_insertion_time = employee.last_insertion_time

                if last_insertion_time is not None:
                    if datetime.now() - last_insertion_time < timedelta(hours=24):
                        messages.error(request, "You can only insert a record once in 24 Hours.")
                        return render(request, 'attendance_form.html', {'form': form})
                form.save()
                employee.last_insertion_time = datetime.now()
                employee.save()

                return redirect('attendance_msg')
            else:
                messages.error(request, "Employee Id not found.")
        else:
            print(form.errors)
    else:
        form = attendance_form()
    return render(request, 'attendance_form.html', {'form': form})

def leave_request(request):
    if request.method == 'POST':
        leave = leave_form(request.POST)
        if leave.is_valid():
            employee_id = leave.cleaned_data['Employee_id']
            if employee_details.objects.filter(Employee_id=employee_id).exists():
                leave_instance = leave.save(commit=False)
                leave_instance.save()

                send_mail(
                    subject="Leave request from an employee.",
                    message=f" Dear Manager,\n\n\tThere has been a leave request from {leave_instance.First_name}. Here are the details: \n\nEmployee Id: {leave_instance.Employee_id}\nFirst Name: {leave_instance.First_name}\nLast Name: {leave_instance.Last_name}\nJob Role: {leave_instance.Job_role}\nDepartment: {leave_instance.Department}\nFrom: {leave_instance.From}\nTo: {leave_instance.To}\nReason: {leave_instance.Reason} \n\nThanks & Regards \nAttendify | Attendance Management System \n+91 635 261 3163 | princesoni2701@gmail.com",
                    from_email='princesoni2701@gmail.com',
                    recipient_list=['pazinzuvadiya@gmail.com'],
                )

                return redirect('leave_msg')
            else:
                messages.error(request, "Employee Id not found.")
        else:
            print(leave.errors)
    else:
        leave = leave_form()
    return render(request, 'leave_request.html', {'leave': leave})

def attendance_msg(request):
    return render (request, 'attendance_msg.html')

def leave_msg(request):
    return render (request, 'leave_msg.html')
