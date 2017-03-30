#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2017/3/29'
"""
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views