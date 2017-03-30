#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2017/3/25'
"""

import datetime
from app import db


class Exam(db.Model):
    """
        exam model
    """
    __tablename__ = 'venus_exam'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    paper_id = db.Column(db.Integer, db.ForeignKey('venus_paper.id'), doc=u"试卷")
    paper = db.relationship('Paper', backref=db.backref('exams', uselist=True))

    name = db.Column(db.String(200), nullable=False, doc=u"考试名称")
    type = db.Column(db.String(200), nullable=True,  doc=u"考试类型")
    overdue = db.Column(db.Integer, nullable=False, doc=u"考试时长")
    password = db.Column(db.String(200), nullable=True, doc=u"考试密码")

    users = db.relationship('User', secondary='venus_exam_user', lazy='dynamic',
                               backref=db.backref('exams', uselist=True))

    create_at = db.Column(db.DateTime(
        timezone=False), default=datetime.datetime.now
    )
    update_at = db.Column(db.DateTime(
        timezone=False), onupdate=datetime.datetime.now, default=datetime.datetime.now
    )