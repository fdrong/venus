#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2017/3/29'
"""
from flask import render_template
from flask_login import login_required


from . import main


@main.route('/', methods=['POST', 'GET'])
@login_required
def index():
    return render_template('base.html')