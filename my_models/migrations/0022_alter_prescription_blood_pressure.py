# Generated by Django 4.1.7 on 2023-06-05 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_models', '0021_prescription_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='blood_pressure',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
