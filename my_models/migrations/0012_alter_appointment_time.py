# Generated by Django 4.1.7 on 2023-05-14 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_models', '0011_appuser_date_of_birth_doctor_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.CharField(max_length=8),
        ),
    ]