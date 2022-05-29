from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import Profession,CustomUser, Employee,Employee_Notification, Employee_Feedback, Employee_leave
from django.contrib import messages




@login_required(login_url='/')
def HOME(request):
    employee_count = Employee.objects.all().count()
    profession_count = Profession.objects.all().count()


    employee_gender_male = Employee.objects.filter(gender= 'Male').count()
    employee_gender_female = Employee.objects.filter(gender= 'Female').count()


    context = {
        'employee_count':employee_count,
        'profession_count':profession_count,
        'employee_gender_male':employee_gender_male,
        'employee_gender_female': employee_gender_female,

    }

    return render(request,'Head/home.html',context)

@login_required(login_url='/')
def ADD_EMPLOYEE(request):
    profession = Profession.objects.all()


    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        profession_id = request.POST.get('profession_id')


        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email is already taken')
            return redirect('add_employee')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username is already taken')
            return redirect('add_employee')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 2
            )
            user.set_password(password)
            user.save()
            profession = Profession.objects.get(id=profession_id)


            employee = Employee(
                admin = user,
                address = address,
                profession_id = profession,
                gender = gender,
            )

            employee.save()
            messages.success(request, user.first_name+" "+user.last_name+"'s details are successfully added")
            return redirect('add_employee')

    context = {
        'profession':profession,

    }
    return render(request, 'Head/add_employee.html', context)

# @login_required(login_url='/')
def VIEW_EMPLOYEE(request):
    employee = Employee.objects.all()

    context = {
        'employee':employee,
    }
    return render(request,'Head/view_employee.html',context)

@login_required(login_url='/')
def EDIT_EMPLOYEE(request,id):
    employee = Employee.objects.filter(id = id)
    profession = Profession.objects.all()


    context = {
        'employee':employee,
        'profession':profession,

    }
    return render(request,'Head/edit_employee.html',context)

@login_required(login_url='/')
def UPDATE_EMPLOYEE(request):
    if request.method == "POST":
        employee_id = request.POST.get('employee_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        profession_id = request.POST.get('profession_id')


        user = CustomUser.objects.get(id = employee_id)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        employee = Employee.objects.get(admin = employee_id)
        employee.address = address
        employee.gender = gender

        # profession = Profession.objects.get(id = profession_id)
        # employee.profession_id = profession

        employee.save()
        messages.success(request,'Record Are Successfully Updated !')
        return redirect('view_employee')

    return render(request,'Head/edit_employee.html')

@login_required(login_url='/')
def DELETE_EMPLOYEE(request,admin):
    employee = CustomUser.objects.get(id=admin)
    employee.delete()
    messages.success(request,'Records are successfully deleted!')
    return redirect('view_employee')


# @login_required(login_url='/')
def ADD_PROFESSION(request):
    if request.method == "POST":
        profession_name = request.POST.get('profession_name')

        profession = Profession(
            name = profession_name,
        )
        profession.save()
        messages.success(request, 'Professions are successfully added!')


        return redirect('add_profession')
    return render(request,'Head/add_profession.html')

# @login_required(login_url='/')
def VIEW_PROFESSION(request):
    profession = Profession.objects.all()
    context = {
        'profession': profession,
    }
    return render(request,'Head/view_profession.html', context)

# @login_required(login_url='/')
def EDIT_PROFESSION(request,id):
    profession = Profession.objects.get(id = id)

    context = {
        'profession':profession,
    }
    return render(request,'Head/edit_profession.html',context)

# @login_required(login_url='/')
def UPDATE_PROFESSION(request):
    if request.method == "POST":
        name = request.POST.get('name')
        profession_id = request.POST.get('profession_id')

        profession = Profession.objects.get(id = profession_id)
        profession.name = name
        profession.save()
        messages.success(request, 'Professions are successfully updated!')
        return redirect('view_profession')

    return render(request,'Head/edit_profession.html')

# @login_required(login_url='/')
def DELETE_PROFESSION(request,id):
    profession = Profession.objects.get(id = id)
    profession.delete()
    messages.success(request,'Profession are Successfully Deleted')

    return redirect('view_profession')

@login_required(login_url='/')
def EMPLOYEE_SEND_NOTIFICATION(request):
    employee = Employee.objects.all()
    notification = Employee_Notification.objects.all().order_by('-id')[0:5]

    context = {
        'employee':employee,
        'notification':notification,
    }
    return render(request,'Head/employee_notification.html',context)


def SAVE_EMPLOYEE_NOTIFICATION(request):
    if request.method == "POST":
        message = request.POST.get('message')
        employee_id = request.POST.get('employee_id')

        employee = Employee.objects.get(admin=employee_id)

        emp_notification = Employee_Notification(
            employee_id=employee,
            message = message,
        )

        emp_notification.save()
        messages.success(request,'Employee Notifications are successfully sent')
        return redirect('employee_send_notification')


def EMPLOYEE_FEEDBACK(request):
    feedback = Employee_Feedback.objects.all()
    feedback_history= Employee_Feedback.objects.all().order_by('-id')[0:5]
    context = {
        'feedback':feedback,
        'feedback_history':feedback_history,
    }
    return render(request,'Head/employee_feedback.html', context)


def REPLY_EMPLOYEE_FEEDBACK(request):
    if request.method == "POST":
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedback = Employee_Feedback.objects.get(id = feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.status = 1
        feedback.save()
    return redirect('get_employee_feedback')


def EMPLOYEE_LEAVE_VIEW(request):
    employee_leave = Employee_leave.objects.all()

    context = {
        'employee_leave':employee_leave,
    }

    return render(request,'Head/employee_leave.html',context)


def EMPLOYEE_APPROVE_LEAVE(request,id):
    leave = Employee_leave.objects.get(id =id)
    leave.status = 1
    leave.save()
    return redirect('employee_leave_view')


def EMPLOYEE_DISAPPROVE_LEAVE(request,id):
    leave = Employee_leave.objects.get(id=id)
    leave.status = 2
    leave.save()
    return redirect('employee_leave_view')

