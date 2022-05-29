from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .models import *


# Register your models here.

class UserModel(UserAdmin):
    list_display = ['username', 'user_type']

admin.site.register(CustomUser, UserModel)
admin.site.register(Profession)
admin.site.register(Employee)
admin.site.register(Employee_Notification)
admin.site.register(Employee_Feedback)
admin.site.register(Employee_leave)


