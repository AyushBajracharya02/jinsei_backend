# Generated by Django 4.1.7 on 2023-05-09 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_models', '0003_alter_doctor_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='user_appointments',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='doctor_appointments',
        ),
    ]