#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2017/3/30'
"""
from threading import Thread
from flask_mail import Message
from flask import current_app
from flask import render_template

from app import app, mail


def send_async_mail(app, msg):
    with app.app_context():
        mail.send(msg)


# 异步发送邮件
def send_mail(to, subject, template, **kwargs):
    msg = Message(app.config['MAIL_SUBJECT_PREFIX'] + u' ' + subject,
                  sender=app.config['MAIL_DEFAULT_SENDER'], recipients=[to])
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    thread = Thread(target=send_async_mail, args=[app, msg])
    thread.start()
    return thread



