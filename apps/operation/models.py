# _*_ encoding:utf-8 _*_

from __future__ import unicode_literals
from datetime import datetime

from django.db import models


from users.models import UserProfile
from courses.models import Course


class UserConsult(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"Name")
    mobile = models.CharField(max_length=11, verbose_name=u"Mobile")
    course_name = models.CharField(max_length=50, verbose_name=u"Course Name")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"Create Time")

    class Meta:
        verbose_name = "User Consult"
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"User")
    course = models.ForeignKey(Course, verbose_name=u"Course")
    comments = models.CharField(max_length=200, verbose_name=u"User Comments")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"Create Time")

    class Meta:
        verbose_name = "Course Comments"
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"User")
    fav_id = models.IntegerField(default=0, verbose_name=u"Data ID")
    fav_type = models.IntegerField(choices=((1, "Course"), (2, "Organization"), (3, "Teacher")), default="1", verbose_name=u"Favorite Type")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"Create Time")

    class Meta:
        verbose_name = "User Favorite"
        verbose_name_plural = "User Favorites"


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name=u"User Who Accept Message")
    message = models.CharField(max_length=500, verbose_name=u"Message Content")
    has_read = models.BooleanField(default=False, verbose_name=u"Has Been read Or Not")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"Time Sent")

    class Meta:
        verbose_name = "User Message"
        verbose_name_plural = "User Messages"


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"User")
    course = models.ForeignKey(Course, verbose_name=u"Course")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"Time Sent")

    class Meta:
        verbose_name = u"User Course"
        verbose_name_plural = u"User Courses"