#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header


class SendMail:
    """邮件发送类
    sender 发送者
    receivers 接收者
    mail_pass 发送者口令、
    mail_host 设置服务器邮件
    """

    def __init__(self, sender, receivers, mail_pass, mail_host):
        self.sender = sender  # 发送者
        self.receivers = receivers  # 接收者
        self.mail_pass = mail_pass  # 口令
        self.mail_host = mail_host  # 设置服务器

    #  发送邮件
    def mail(self, ):
        # 三个参数：文本内容，文本格式， 编码
        message = MIMEText('Python邮件发送...', 'plain', 'utf-8')
        message['From'] = self.sender  # 发送者
        message['To'] = self.receivers  # 接收者

        subject = 'Python SMTP 邮件'
        message['Subject'] = Header(subject, 'utf-8')

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, 25)  # 25为SMTP端口号
            smtpObj.login(self.sender, self.mail_pass)
            smtpObj.sendmail(self.sender, self.receivers, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")


# ############ 测试代码  ##############
if __name__ == '__main__':
    info = dict(
        sender='gini598779784@163.com',
        receivers='gini598779784@163.com',
        mail_pass='liu1314.@qq',
        mail_host='smtp.163.com'
    )
    S = SendMail(**info)
    S.mail()
