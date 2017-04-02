# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trello_app', '0003_list_child'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='child',
            field=models.CharField(default='lists', max_length=20),
        ),
        migrations.AlterField(
            model_name='list',
            name='child',
            field=models.CharField(default='cards', max_length=20),
        ),
    ]