# Generated by Django 4.1.7 on 2023-06-14 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_models', '0034_rename_creation_date_prescription_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescription',
            old_name='date',
            new_name='createddate',
        ),
    ]
