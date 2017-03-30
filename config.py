#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '16/7/18'
"""

import os
import random
import string
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    # Session 配置
    SESSION_TYPE = 'redis'
    SESSION_COOKIE_HTTPONLY = True
    # SECRET_KEY = ''.join(random.sample(string.ascii_lowercase+string.digits, 7))
    SECRET_KEY = 'u5syzir'
    PERMANENT_SESSION_LIFETIME = 60 * 60 * 24 * 7  # 设置cookie过期时间

    # SQLALCHEMY 配置
    SQLALCHEMY_DATABASE_URI = ""

    # SQLALCHEMY_ECHO = True
    SQLALCHEMY_POOL_SIZE = 100
    SQLALCHEMY_MAX_OVERFLOW = 25
    SQLALCHEMY_POOL_RECYCLE = 30
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 多数据库
    # databases = {
    #     'app': 'postgresql://app:newpass@localhost/app',
    #     'vms': 'postgresql://vms:newpass@localhost/vms'
    # }
    # SQLALCHEMY_BINDS = databases

    # CELERY 配置
    BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'
    CELERY_TIMEZONE = 'Asia/Shanghai'
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # POST 最大长度为100MB

    # 邮件配置
    MAIL_SUBJECT_PREFIX = u'[Venus]'


# 开发环境
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://venus:newpass@localhost/venus'
    # Flask-Mail 配置
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 25
    MAIL_USERNAME = '1216606787@qq.com'
    MAIL_PASSWORD = 'rong221133'
    MAIL_DEFAULT_SENDER = '1216606787@qq.com'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    # 发邮件的模板需要用到
    # SERVER_NAME = '127.0.0.1'


# 测试环境
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = ""


# 生产环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ""


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
