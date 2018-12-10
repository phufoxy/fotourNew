# Generated by Django 2.1 on 2018-09-19 10:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourer', '0005_auto_20180919_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tourer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=250, null=True)),
                ('name', models.CharField(max_length=250)),
                ('avatar', models.FileField(default='/default/user-avatar-default-165.png', upload_to='tourer/')),
                ('password', models.CharField(max_length=250)),
                ('question', models.CharField(default='question', max_length=250)),
                ('time_create', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.DeleteModel(
            name='Tourser',
        ),
    ]