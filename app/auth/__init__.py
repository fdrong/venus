#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2017/3/24'
"""

from flask import Blueprint

auth = Blueprint('auth', __name__)    # 定义一个认证蓝图

from . import views
