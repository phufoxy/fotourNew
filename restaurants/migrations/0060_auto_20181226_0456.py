# Generated by Django 2.1.4 on 2018-12-26 04:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0059_auto_20181224_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_restaurant',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 26, 4, 56, 48, 479247)),
        ),
    ]
