# Generated by Django 4.1.7 on 2023-06-05 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_models', '0026_prescription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='blood_pressure',
        ),
        migrations.AddField(
            model_name='prescription',
            name='bp',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
