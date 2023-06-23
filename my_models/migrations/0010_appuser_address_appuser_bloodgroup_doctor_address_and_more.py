# Generated by Django 4.1.7 on 2023-05-12 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_models', '0009_appuser_age_alter_appuser_firstname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='appuser',
            name='bloodgroup',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O-', 'O-')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='age',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='bloodgroup',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O-', 'O-')], max_length=3, null=True),
        ),
    ]