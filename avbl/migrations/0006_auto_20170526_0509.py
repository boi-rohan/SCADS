# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-25 23:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avbl', '0005_auto_20170526_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='court',
            name='image_src',
            field=models.URLField(max_length=1000),
        ),
    ]
