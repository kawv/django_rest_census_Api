# Generated by Django 3.2 on 2021-05-05 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('census_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='citizens',
            new_name='Citizen',
        ),
    ]
