# Generated by Django 4.1.7 on 2023-06-05 01:32

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_models', '0023_remove_prescription_blood_pressure_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='bloodpressure',
        ),
        migrations.AddField(
            model_name='prescription',
            name='blood_pressure',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=0, max_digits=3), null=True, size=None),
        ),
    ]
