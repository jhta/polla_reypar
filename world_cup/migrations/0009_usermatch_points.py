# Generated by Django 2.0.1 on 2018-03-28 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world_cup', '0008_auto_20180328_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermatch',
            name='points',
            field=models.PositiveIntegerField(default=0),
        ),
    ]