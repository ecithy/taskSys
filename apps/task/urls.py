# -*- coding: utf-8 -*-
__author__ = 'hy'

from django.conf.urls import url

from .views import SendMailView

urlpatterns = [
    # 邮件发送
    url(r'^get/$', SendMailView.as_view(), name="send_mail"),

]
