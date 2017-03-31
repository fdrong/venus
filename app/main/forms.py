#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2017/3/31'
"""
from flask_wtf import FlaskForm
from wtforms.validators import Required, Regexp, Length, Email
from wtforms import ValidationError, StringField, PasswordField, \
    SelectField, SubmitField

from app.models import User


class ProfileForm(FlaskForm):
    email = StringField(u'邮箱:', validators=[Required(), Length(1, 64),
                                           Email()])
    username = StringField(u'用户名:', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
    name = StringField(u'真实姓名:', validators=[Required()])
    mobilephone = StringField(u'手机号:', validators=[Required(), Regexp('[0-9]{11}',
                                            0, message=u"请确认手机号码是否为11位数字")])
    company = SelectField(u'公司:', coerce=int, validators=[Required()])
    submit = SubmitField(u'提交')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u'邮箱已存在.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(u'用户名已存在.')