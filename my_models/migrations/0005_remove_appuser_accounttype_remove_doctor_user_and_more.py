# Generated by Django 4.1.7 on 2023-05-09 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_models', '0004_remove_appuser_user_appointments_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='accounttype',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='user',
        ),
        migrations.AddField(
            model_name='doctor',
            name='firstname',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='lastname',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='password',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='firstname',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='lastname',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='password',
            field=models.CharField(max_length=32),
        ),
    ]