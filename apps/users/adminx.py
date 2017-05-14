# _*_ coding: utf-8 _*_
__author__ = 'Louis Xie'
__date = '5/14/17 11:04 AM'

import xadmin

from models import EmailVerifyRecord


class EmailVerifyRecordAdmin(object):
    pass

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
