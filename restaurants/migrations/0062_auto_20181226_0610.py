# Generated by Django 2.1.4 on 2018-12-26 06:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0061_auto_20181226_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_restaurant',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 26, 6, 9, 58, 878970)),
        ),
    ]
