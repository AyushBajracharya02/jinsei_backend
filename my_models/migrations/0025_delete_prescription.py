# Generated by Django 4.1.7 on 2023-06-05 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_models', '0024_remove_prescription_bloodpressure_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Prescription',
        ),
    ]
