# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-05 19:09
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=200, verbose_name='User Comments')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Create Time')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Course Comments',
                'verbose_name_plural': 'Course Comments',
            },
        ),
        migrations.CreateModel(
            name='UserConsult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('mobile', models.CharField(max_length=11, verbose_name='Mobile')),
                ('course_name', models.CharField(max_length=50, verbose_name='Course Name')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Create Time')),
            ],
            options={
                'verbose_name': 'User Consult',
                'verbose_name_plural': 'User Consult',
            },
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Time Sent')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'User Course',
                'verbose_name_plural': 'User Courses',
            },
        ),
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fav_id', models.IntegerField(default=0, verbose_name='Data ID')),
                ('fav_type', models.IntegerField(choices=[(1, 'Course'), (2, 'Organization'), (3, 'Teacher')], default='1', verbose_name='Favorite Type')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Create Time')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'User Favorite',
                'verbose_name_plural': 'User Favorites',
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(default=0, verbose_name='User Who Accept Message')),
                ('message', models.CharField(max_length=500, verbose_name='Message Content')),
                ('has_read', models.BooleanField(default=False, verbose_name='Has Been read Or Not')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Time Sent')),
            ],
            options={
                'verbose_name': 'User Message',
                'verbose_name_plural': 'User Messages',
            },
        ),
    ]
