# Generated by Django 2.1.4 on 2018-12-26 06:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0050_auto_20181226_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speak',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 26, 6, 11, 53, 182833)),
        ),
        migrations.AlterField(
            model_name='taskspeak',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 26, 6, 11, 53, 183200)),
        ),
    ]