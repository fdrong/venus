#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2017/3/31'
"""

from functools import wraps
from flask_login import current_user
from flask import abort


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorator_fuction(*args, **kwargs):
            if current_user.can(permission):
                return f(*args, **kwargs)
            else:
                abort(403)
            return decorator_fuction
        return decorator