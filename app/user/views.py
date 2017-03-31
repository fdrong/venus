#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2017/3/25'
"""
from flask import render_template
from flask_login import login_required, current_user

from . import user
from .forms import ProfileForm
from app.utils.consts import CompanyChoices


@user.route('/profile')
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        pass
    form.username.data = current_user.username
    form.name.data = current_user.name
    form.email.data = current_user.email
    form.mobilephone.data = current_user.mobilephone
    form.company.data = current_user.company_id
    form.company.choices = CompanyChoices
    return render_template('user/profile.html', form=form)


@user.route('/list')
@login_required
def user_list():
    pass


@user.route('/add')
@login_required
def user_add():
    pass


@user.route('/edit/<int:user_id>')
@login_required
def user_edit(user_id):
    pass