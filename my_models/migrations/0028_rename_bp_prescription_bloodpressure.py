# Generated by Django 4.1.7 on 2023-06-05 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_models', '0027_remove_prescription_blood_pressure_prescription_bp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescription',
            old_name='bp',
            new_name='bloodpressure',
        ),
    ]
