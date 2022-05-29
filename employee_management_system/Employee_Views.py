from django.shortcuts import render, redirect
from app.models import Employee,Employee_Notification, Employee_Feedback, Employee_leave
from django.contrib import messages

def Home(request):
    return render(request, 'Employee/home.html')


def EMPLOYEE_NOTIFICATION(request):
    employee = Employee.objects.filter(admin = request.user.id)
    for i in employee:
        employee_id = i.id
        notification = Employee_Notification.objects.filter(employee_id = employee_id)

        context = {
            'notification':notification,
        }
    return render(request, 'Employee/notification.html', context)


def EMPLOYEE_NOTIFICATION_MARK_AS_DONE(request,status):
    notification = Employee_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('employee_notification')


def EMPLOYEE_FEEDBACK(request):
    employee_id = Employee.objects.get(admin = request.user.id)
    feedback_history = Employee_Feedback.objects.filter(employee_id=employee_id)

    context = {
        'feedback_history':feedback_history,
    }
    return render(request,'Employee/feedback.html',context)

def EMPLOYEE_FEEDBACK_SAVE(request):

    if request.method == "POST":
        feedback = request.POST.get('feedback')
        employee = Employee.objects.get(admin=request.user.id)

        feedbacks = Employee_Feedback(
            employee_id=employee,
            feedback = feedback,
            feedback_reply = "",
        )
        feedbacks.save()
        return redirect('employee_feedback')


def EMPLOYEE_APPLY_LEAVE(request):
    employee = Employee.objects.filter(admin=request.user.id)
    for i in employee:
        employee_id = i.id
        employee_leave_history = Employee_leave.objects.filter(employee_id = employee_id)

        context = {
            'employee_leave_history':employee_leave_history,
        }

        return render(request,'Employee/apply_leave.html',context)


def EMPLOYEE_LEAVE_SAVE(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')

        employee_id = Employee.objects.get(admin = request.user.id)

        employee_leave = Employee_leave(
            employee_id = employee_id,
            date = leave_date,
            message = leave_message,
        )

        employee_leave.save()
        messages.success(request,'Leave application is successfully sent!')

    return redirect('apply_leave')