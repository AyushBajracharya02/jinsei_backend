# Generated by Django 4.1.7 on 2023-06-05 01:57

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_models', '0029_rename_bloodpressure_prescription_blood_pressure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='blood_pressure',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=0, max_digits=3), size=None),
        ),
    ]
