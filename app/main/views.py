#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2017/3/29'
"""
from flask import render_template, flash

from . import main


@main.route('/index', methods=['POST', 'GET'])
def index():
    flash("OK")
    return render_template('base.html')