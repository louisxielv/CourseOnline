# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-14 16:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20170505_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='org',
        ),
    ]