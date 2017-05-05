# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-05 19:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityDict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='City')),
                ('desc', models.CharField(max_length=200, verbose_name='City Description')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'City',
            },
        ),
        migrations.CreateModel(
            name='CourseOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Organization Name')),
                ('desc', models.TextField(verbose_name='Organization Description')),
                ('click_num', models.IntegerField(default=0, verbose_name='Number of Clicks')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='Number of Favorites')),
                ('image', models.ImageField(upload_to='org/%Y/%m', verbose_name='Cover')),
                ('address', models.CharField(default='', max_length=150)),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CityDict', verbose_name='City of Organization')),
            ],
            options={
                'verbose_name': 'Organization',
                'verbose_name_plural': 'Organization',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Teacher Name')),
                ('work_years', models.IntegerField(default=0, verbose_name='Number of Years of Working')),
                ('work_company', models.CharField(max_length=50, verbose_name='Working Company')),
                ('work_position', models.CharField(max_length=50, verbose_name='Working Position')),
                ('points', models.CharField(max_length=50, verbose_name='Characteristics')),
                ('click_num', models.IntegerField(default=0, verbose_name='Number of Clicks')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='Number of Favorites')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('org', models.ForeignKey(on_delete='id', to='organization.CourseOrg', to_field='Organization Belonged to')),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teacher',
            },
        ),
    ]
