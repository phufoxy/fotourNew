# Generated by Django 2.1.4 on 2018-12-26 06:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0067_auto_20181226_0456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_house',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 26, 6, 9, 3, 27510)),
        ),
    ]
