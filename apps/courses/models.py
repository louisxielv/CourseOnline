# _*_ encoding:utf-8 _*_

from __future__ import unicode_literals
from datetime import datetime

from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"Course Name")
    description = models.CharField(max_length=300, verbose_name=u"Course Description")
    detail = models.TextField(verbose_name=u"Couese Details")
    degree = models.CharField(choices=(("easy", u"Easy"), ("medium", u"Medium"), ("hard", u"Hard")), max_length=10)
    duration = models.IntegerField(default=0, verbose_name=u"Course Duration")
    number_of_participants = models.IntegerField(default=0, verbose_name=u"Number of Participants")
    number_of_favs = models.IntegerField(default=0, verbose_name=u"Number of Favorites")
    image = models.ImageField(upload_to="course/%Y/%m", verbose_name=u"Cover", max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name="Number of Clicks")
    add_time = models.DateTimeField(default= datetime.now, verbose_name=u"Time Course Created")

    class Meta:
        verbose_name = u"Course"
        verbose_name_plural = verbose_name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"Course")
    name = models.CharField(max_length=100, verbose_name= u"Name of Lesson")

    class Meta:
        verbose_name = u"Lessons of Course"
        verbose_name_plural = verbose_name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u"Course")
    name = models.CharField(max_length=100, verbose_name=u"Name of Video")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"Time Video Created")

    class Meta:
        verbose_name = u"Videos of Course"
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"Course")
    name = models.CharField(max_length=100, verbose_name=u"Name of Resource")
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name=u"Download Address", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"Time Resource Created")

    class Meta:
        verbose_name = u"Resources of Course"
        verbose_name_plural = verbose_name