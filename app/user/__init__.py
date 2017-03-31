#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2017/3/24'
"""
from flask import Blueprint
user = Blueprint('user', __name__)

from . import views