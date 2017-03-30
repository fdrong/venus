#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2017/3/25'
"""
import datetime
from app import db


class Paper(db.Model):
    """
        paper model
    """
    __tablename__ = 'venus_paper'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False, doc=u"试卷名")
    content = db.Column(db.TEXT, nullable=True,  doc=u"试卷内容")

    create_at = db.Column(db.DateTime(
        timezone=False), default=datetime.datetime.now
    )
    update_at = db.Column(db.DateTime(
        timezone=False), onupdate=datetime.datetime.now, default=datetime.datetime.now
    )
