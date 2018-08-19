# -*- coding: utf-8 -*-
# 第三方库
from django.views.generic.base import View
from django.http import HttpResponse
# 自定义库
from tools.WYSendMail import SendMail
from tasksys.settings import mail_info


class SendMailView(View):
    def get(self, request):
        send_mail = SendMail(**mail_info)
        send_mail.mail()

        return HttpResponse('{"status":"success"}', content_type='application/json')
