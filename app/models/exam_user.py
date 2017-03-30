#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2017/3/25'
"""
import datetime
from app import db


class ExamUser(db.Model):
    """
        exam model
    """
    __tablename__ = 'venus_exam_user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    exam_id = db.Column(db.Integer, db.ForeignKey('venus_exam.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('venus_user.id'), nullable=False)

    begin_at = db.Column(db.DateTime(
        timezone=False), nullable=True, doc=u"考试开始时间"
    )
    commit_at = db.Column(db.DateTime(
        timezone=False), nullable=True, doc=u"考试提交时间"
    )

    create_at = db.Column(db.DateTime(
        timezone=False), default=datetime.datetime.now
    )
    update_at = db.Column(db.DateTime(
        timezone=False), onupdate=datetime.datetime.now, default=datetime.datetime.now
    )