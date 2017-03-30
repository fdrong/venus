#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2017/3/25'
"""
import datetime
from app import db


class Log(db.Model):
    """
        Log model
    """
    __tablename__ = 'venus_log'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    user_id = db.Column(db.Integer, db.ForeignKey('venus_user.id'))
    user = db.relationship('User', backref=db.backref('logs'))

    type = db.Column(db.String(200), nullable=False, doc=u"操作类型")  # 操作类型
    ip = db.Column(db.String(2000), nullable=True, doc=u"远程主机IP")  # 远程主机IP
    message = db.Column(db.String(200), nullable=False, doc=u"操作信息")  # 操作信息
    create_at = db.Column(db.DateTime(
        timezone=False), default=datetime.datetime.now
    )     # 创建时间

    # date_joined = db.Column(DateTime(
    #     timezone=False), default=datetime.datetime.now, name='date_joined'
    # )

    # avatar = db.Column(URLType, nullable=True, default=None, name='avatar')

    @property
    def as_dict(self):
        """
            object to dict
        """
        return {
            db.Column.name: str(getattr(self, db.Column.name))
            for db.Column in self.__table__.db.Columns
        }