# Generated by Django 2.1 on 2018-11-24 03:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0034_auto_20181124_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speak',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 24, 10, 40, 52, 91211)),
        ),
        migrations.AlterField(
            model_name='taskspeak',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 24, 10, 40, 52, 91211)),
        ),
    ]