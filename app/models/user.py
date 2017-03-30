#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2017/3/24'
"""
import datetime
from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app import db, app


class User(UserMixin, db.Model):
    """
        users model
    """
    __tablename__ = 'venus_user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(60), nullable=False, unique=True, index=True, doc=u"用户名")
    name = db.Column(db.String(60), nullable=False, doc=u"姓名")
    password_hash = db.Column(db.String(500), nullable=False, doc=u"密码")
    email = db.Column(db.String(100), nullable=False, unique=True, doc=u'邮箱')
    confirmed = db.Column(db.Boolean, default=False)                                  # 是否确认
    mobilephone = db.Column(db.String(20), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey("venus_company.id"))
    company = db.relationship('Company', backref=db.backref("users"))
    isdelete = db.Column(db.Integer, nullable=False, default=0, doc=u"是否删除")

    last_login_time = db.Column(db.DateTime(timezone=False), nullable=True, doc=u"上次登录时间")

    create_at = db.Column(db.DateTime(
        timezone=False), default=datetime.datetime.now
    )
    update_at = db.Column(db.DateTime(
        timezone=False), onupdate=datetime.datetime.now, default=datetime.datetime.now
    )

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 验证密码
    def vertify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(app.config.get('SECRET_KEY'), expiration)
        return s.dumps({"confirm": self.id})

    def generate_reset_token(self, expiration=3600):
        s = Serializer(app.config.get('SECRET_KEY'), expiration)
        return s.dumps({"reset": self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True
    def reset_password(self, token, newpassword):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('reset') != self.id:
            return False
        self.password = newpassword
        db.session.add(self)
        return True