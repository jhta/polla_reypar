# Generated by Django 2.0.1 on 2018-03-11 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0008_profile_birth_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
