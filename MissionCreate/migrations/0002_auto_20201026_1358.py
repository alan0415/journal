# Generated by Django 2.2 on 2020-10-26 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MissionCreate', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='longtermmissionlist',
            old_name='releated_link_1',
            new_name='related_link_1',
        ),
        migrations.RenameField(
            model_name='longtermmissionlist',
            old_name='releated_link_2',
            new_name='related_link_2',
        ),
        migrations.RenameField(
            model_name='longtermmissionlist',
            old_name='releated_link_3',
            new_name='related_link_3',
        ),
    ]
