# Generated by Django 3.0.8 on 2021-04-05 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='in_staff',
            new_name='is_staff',
        ),
    ]
