# Generated by Django 2.1.4 on 2018-12-26 09:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0054_auto_20181226_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speak',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 26, 9, 19, 11, 946461)),
        ),
        migrations.AlterField(
            model_name='taskspeak',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 26, 9, 19, 11, 946829)),
        ),
    ]
