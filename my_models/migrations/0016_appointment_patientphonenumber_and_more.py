# Generated by Django 4.1.7 on 2023-06-02 14:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_models', '0015_remove_appointment_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='patientphonenumber',
            field=models.CharField(max_length=10, null=True, validators=[django.core.validators.RegexValidator(code='invalid_phone_number', message='Phone should only contain numbers and should be 10 characters', regex='^\\d{10}$')]),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(code='invalid_phone_number', message='Phone should only contain numbers and should be 10 characters', regex='^\\d{10}$')]),
        ),
    ]
