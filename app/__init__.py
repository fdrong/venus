#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '16/7/18'
"""
import os
import logging
from flask import Flask
from flask.logging import create_logger
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_session import Session
from flask_login import LoginManager
from logging.handlers import SMTPHandler
from celery import Celery, platforms
from config import config


# -------------------------------------------------------------------
# 调用Flask()时，如果instance_relative_config=True，
# app.config.from_pyfile()会自动加载instance文件夹中的config.py
# -------------------------------------------------------------------
app = Flask(__name__)  # 创建一个APP对象
# 载入配置文件
app.config.from_object(config[os.getenv('CONFIG_NAME') or 'default'])

# -------------------------------------------------------------------
# 初始化Mail模块
# -------------------------------------------------------------------
mail = Mail(app)  # 初始化mail

# -------------------------------------------------------------------
# 初始化SQLAlchemy模块
# -------------------------------------------------------------------
db = SQLAlchemy(app)  # 初始化数据库ORM

# -------------------------------------------------------------------
# 初始化session
# -------------------------------------------------------------------
Session(app=app)

# -------------------------------------------------------------------
# 初始化Celery任务队列
# 启动方式：celery -A app.celery worker --loglevel=info
#         celery -A app.celery beat --loglevel=info
# -------------------------------------------------------------------
celery = Celery(app.name, include=['app.utils.tasks'])
celery.config_from_object(config[os.getenv('CONFIG_NAME') or 'default'])
platforms.C_FORCE_ROOT = True  # 在ROOT下启动


# -------------------------------------------------------------------
# 初始化Flask-Login模块
# -------------------------------------------------------------------
login_manager = LoginManager()  # 初始化登录管理对象
login_manager.init_app(app)
login_manager.login_view = 'auth.login'   # 登录跳转视图
login_manager.session_protection = 'strong'

login_manager.login_message = u"请使用手机号或者邮箱账号登陆！"         # 登录跳转视图前的输出消息


# -------------------------------------------------------------------
# 初始化日志模块：文件日志、控制台打印日志、邮件日志告警
# -------------------------------------------------------------------
logger = create_logger(app)
LOG_FILE = os.path.join(app.root_path, "static", "logs", "venus.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s[line:%(lineno)d] - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')  # 格式化日志
file_handler = logging.handlers.TimedRotatingFileHandler(LOG_FILE, 'D', 1, 0)  # 实例化handler
file_handler.suffix = "%Y-%m-%d.log"
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)  # 设置文件日志打印级别

console_handler = logging.StreamHandler()  # 设置终端日志打印
console_handler.setLevel(logging.DEBUG)  # 设置终端日志打印级别
console_handler.setFormatter(formatter)  # 设置终端日志打印格式

logger.addHandler(file_handler)     # 添加Handler
logger.addHandler(console_handler)
logger.setLevel(logging.INFO)


# -------------------------------------------------------------------
# 注册蓝图模块
# -------------------------------------------------------------------
from .auth import auth        # auth蓝图
app.register_blueprint(auth)

from .main import main
app.register_blueprint(main)  # 主页

from .user import user
app.register_blueprint(user, url_prefix='/user')  # 用户
#
# from .api import api  # api蓝图
# app.register_blueprint(api, url_prefix='/api')
#
# from utils.event import *

