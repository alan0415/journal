# Generated by Django 2.2 on 2020-10-27 14:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('user_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('register_time', models.DateTimeField(default=datetime.datetime(2020, 10, 27, 14, 49, 45, 874551))),
                ('user_password', models.CharField(max_length=15)),
                ('user_email', models.CharField(max_length=60)),
                ('valid', models.BooleanField(default=False)),
            ],
        ),
    ]
