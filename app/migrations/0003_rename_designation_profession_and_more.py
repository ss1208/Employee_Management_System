# Generated by Django 4.0.4 on 2022-05-26 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_employee_notification_employee_feedback'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Designation',
            new_name='Profession',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='designation_id',
            new_name='profession_id',
        ),
    ]