# Generated by Django 2.1 on 2018-12-07 14:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0060_auto_20181207_1957'),
        ('tourer', '__latest__'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_house',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourer.Account'),
        ),
        migrations.AlterField(
            model_name='comment_house',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 7, 21, 24, 5, 773291)),
        ),
    ]
