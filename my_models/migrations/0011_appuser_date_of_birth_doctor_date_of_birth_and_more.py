# Generated by Django 4.1.7 on 2023-05-12 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_models', '0010_appuser_address_appuser_bloodgroup_doctor_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
