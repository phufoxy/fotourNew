# Generated by Django 2.1 on 2018-12-24 05:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0065_auto_20181209_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_house',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 24, 12, 0, 54, 841188)),
        ),
    ]