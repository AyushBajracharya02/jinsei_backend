# Generated by Django 4.1.7 on 2023-05-14 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_models', '0012_alter_appointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(),
        ),
    ]
