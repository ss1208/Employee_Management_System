from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    USER = (
        (1, 'HEAD'),
        (2, 'EMPLOYEE'),
     
    )

    user_type = models.CharField(choices=USER, max_length=50, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')


class Profession(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    profession_id = models.ForeignKey(Profession, on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name

class Employee_Notification(models.Model):
    employee_id  = models.ForeignKey(Employee, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True, default =0)

    def __str__(self):
        return self.employee_id.admin.first_name

class Employee_Feedback(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.employee_id.admin.first_name+" "+self.employee_id.admin.last_name

class Employee_leave(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    message = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee_id.admin.first_name + self.employee_id.admin.last_name






