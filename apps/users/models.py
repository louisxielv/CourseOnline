# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name="Nick Name", default="")
    b_day = models.DateField(verbose_name="Birthday", null=True, blank=True)
    gender = models.CharField(max_length=15, choices=(("male", u"Gentlemen"), ("female", u"Madam")), default="female")
    address = models.CharField(max_length=100, default=u"")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100)

    class Meta:
        verbose_name = "User Information"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"Verification Code")
    email = models.EmailField(max_length=50, verbose_name=u"Email")
    send_type = models.CharField(choices=(("register", u"Register"), ("forget", u"Forget")), max_length=10)
    send_time = models.DateField(default=datetime.now)

    class Meta:
        verbose_name = u"Email Verification"
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"Title")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name=u"Slide Show Image", max_length=100)
    url = models.URLField(max_length=200, verbose_name=u"Web Address")
    index = models.IntegerField(default=100, verbose_name=u"Sequence")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"Add Time")

    class Meta:
        verbose_name = u"Banner"
        verbose_name_plural = verbose_name


