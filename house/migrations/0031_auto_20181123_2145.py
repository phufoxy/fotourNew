# Generated by Django 2.1 on 2018-11-23 14:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0030_auto_20181122_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_house',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 23, 21, 45, 22, 932588)),
        ),
    ]