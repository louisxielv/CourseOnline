# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-14 16:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_remove_teacher_org'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='org',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='Organization'),
            preserve_default=False,
        ),
    ]
