# Generated by Django 4.1.7 on 2023-06-22 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_models', '0036_alter_prescription_createddate'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='mealschedule',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='mealschedule',
            field=models.JSONField(blank=True, null=True),
        ),
    ]