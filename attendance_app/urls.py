from django.urls import path
from attendance_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('attendance/', views.attendance, name='attendance'),
    path('leave_request/', views.leave_request, name='leave_request'),
    path('attendance_msg/', views.attendance_msg, name='attendance_msg'),
    path('leave_msg/', views.leave_msg, name='leave_msg')
]
