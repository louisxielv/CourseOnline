# _*_ encoding:utf-8 _*_

from __future__ import unicode_literals
from datetime import datetime

from django.db import models


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"City")
    desc = models.CharField(max_length=200, verbose_name=u"City Description")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"City"
        verbose_name_plural = verbose_name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"Organization Name")
    desc = models.TextField(verbose_name=u"Organization Description")
    click_num = models.IntegerField(default=0, verbose_name=u"Number of Clicks")
    fav_nums = models.IntegerField(default=0, verbose_name=u"Number of Favorites")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name=u"Cover", max_length=100)
    address = models.CharField(max_length=150, default=u"")
    city = models.ForeignKey(CityDict, verbose_name="City of Organization")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"Organization"
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name=u"Organization Belonged to")
    name = models.CharField(max_length=50, verbose_name=u"Teacher Name")
    work_years = models.IntegerField(default=0, verbose_name=u"Number of Years of Working")
    work_company = models.CharField(max_length=50, verbose_name=u"Working Company")
    work_position = models.CharField(max_length=50, verbose_name=u"Working Position")
    points = models.CharField(max_length=50, verbose_name=u"Characteristics")
    click_num = models.IntegerField(default=0, verbose_name=u"Number of Clicks")
    fav_nums = models.IntegerField(default=0, verbose_name=u"Number of Favorites")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"Teacher"
        verbose_name_plural = verbose_name