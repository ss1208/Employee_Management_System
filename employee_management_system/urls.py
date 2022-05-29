
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, Head_Views,Employee_Views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('base/', views.BASE, name='base'),
                  path('blank', views.BLANK, name='blank'),

                  # Login path
                  path('',views.landing,name='landing'),
                  path('capture',views.camera,name='capture'),
                  path('attendance',views.attendance,name='attendance'),
                  path('login', views.LOGIN, name='login'),
                  path('doLogin', views.doLogin, name='doLogin'),
                  path('doLogout', views.doLogout, name='logout'),

                  # Profile Update
                  path('Profile', views.PROFILE, name='profile'),
                  path('Profile/update', views.PROFILE_UPDATE, name='profile_update'),

                  # This is HEAD Panel URL
                  path('Head/Home', Head_Views.HOME, name='head_home'),

                  path('Head/Employee/Add', Head_Views.ADD_EMPLOYEE, name='add_employee'),
                  path('Head/Employee/View', Head_Views.VIEW_EMPLOYEE, name='view_employee'),
                  path('Head/Employee/Edit/<str:id>', Head_Views.EDIT_EMPLOYEE, name='edit_employee'),
                  path('Head/Employee/Update', Head_Views.UPDATE_EMPLOYEE, name='update_employee'),
                  path('Head/Employee/Delete/<str:admin>', Head_Views.DELETE_EMPLOYEE, name='delete_employee'),

                  path('Head/Profession/Add', Head_Views.ADD_PROFESSION, name='add_profession'),
                  path('Head/Profession/View', Head_Views.VIEW_PROFESSION, name='view_profession'),
                  path('Head/Profession/Edit/<str:id>', Head_Views.EDIT_PROFESSION, name='edit_profession'),
                  path('Head/Profession/Update', Head_Views.UPDATE_PROFESSION, name='update_profession'),
                  path('Head/Profession/Delete/<str:id>', Head_Views.DELETE_PROFESSION, name='delete_profession'),

                  path('Head/Employee/send_notification', Head_Views.EMPLOYEE_SEND_NOTIFICATION, name='employee_send_notification'),
                  path('Head/Employee/save_notification', Head_Views.SAVE_EMPLOYEE_NOTIFICATION,name='save_employee_notification'),

                  path('Head/Employee/feedback', Head_Views.EMPLOYEE_FEEDBACK,name='get_employee_feedback'),
                  path('Head/Employee/feedback/reply/save', Head_Views.REPLY_EMPLOYEE_FEEDBACK,name='reply_employee_feedback'),

                  path('Head/Employee/Leave_view', Head_Views.EMPLOYEE_LEAVE_VIEW,name='employee_leave_view'),
                  path('Head/Employee/Approve_leave/<str:id>', Head_Views.EMPLOYEE_APPROVE_LEAVE, name='employee_approve_leave'),
                  path('Head/Employee/Disapprove_leave/<str:id>', Head_Views.EMPLOYEE_DISAPPROVE_LEAVE, name='employee_disapprove_leave'),

                  # Employee Urls
                  path('Employee/Home', Employee_Views.Home, name='employee_home'),
                  path('Employee/Notifications', Employee_Views.EMPLOYEE_NOTIFICATION, name='employee_notification'),
                  path('Employee/mark_as_done/<str:status>', Employee_Views.EMPLOYEE_NOTIFICATION_MARK_AS_DONE,name='employee_notification_mark_as_done'),
                  path('Employee/feedback', Employee_Views.EMPLOYEE_FEEDBACK, name='employee_feedback'),
                  path('Employee/feedback/save', Employee_Views.EMPLOYEE_FEEDBACK_SAVE, name='employee_feedback_save'),
                  path('Employee/apply_for_leave', Employee_Views.EMPLOYEE_APPLY_LEAVE, name='apply_leave'),
                  path('Employee/Leave_save', Employee_Views.EMPLOYEE_LEAVE_SAVE, name='employee_leave_save'),



] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
