# Generated by Django 2.1.4 on 2018-12-26 06:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0038_auto_20181226_0456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentplace',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 26, 6, 7, 28, 191975)),
        ),
    ]
