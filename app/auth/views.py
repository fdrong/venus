#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2017/3/25'
"""
from flask_login import current_user, login_user, \
    logout_user, login_required
from flask import g, session, render_template, flash, redirect, \
    request, url_for

from . import auth
from .forms import LoginForm, RegistrationForm, PasswordResetRequestForm, PasswordResetForm
from app import app, login_manager, db
from app.models import User
from app.utils.email import send_mail
from app.utils.consts import CompanyChoices


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# 请求Hook
@app.before_request
def before_request():
    session.permanent = True
    g.user = current_user


# 404错误处理
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# 505错误处理
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


@app.errorhandler(403)
def fobidden_error(error):
    return render_template('403.html'), 403


@auth.before_app_request
def before_request():
    if current_user.is_authenticated:
        # current_user.ping()
        if not current_user.confirmed \
                and request.endpoint \
                and request.endpoint[:5] != 'auth.' \
                and request.endpoint != 'static':
            return redirect(url_for('auth.unconfirmed'))


@auth.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            flash(u"用户[{}]未注册,请先注册。".format(form.email.data))
        # elif not user.confirmed:
        #     return redirect(url_for('auth.unconfirmed'))
        elif not user.vertify_password(form.password.data):
            flash(u"密码错误,请重新输入密码。")
        else:
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for("main.index"))
    return render_template('auth/login.html', form=form)


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    session.clear()
    flash(u"您已退出登录")
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    form.company.choices = CompanyChoices
    if form.validate_on_submit():
        user = User(
                    username=form.username.data,
                    password=form.password.data,
                    email=form.email.data,
                    name=form.name.data,
                    mobilephone=form.mobilephone.data,
                    company_id=form.company.data,
                    )
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_mail(user.email, u'确认账户',
                   'auth/email/confirm', user=user, token=token)
        flash(u'确认邮件已经发送至您的邮箱，请先登录系统，在登录邮箱确认重置')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


# 重置密码请求
@auth.route('/reset', methods=['GET', 'POST'])
def password_reset_request():
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    form = PasswordResetRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            token = user.generate_reset_token()
            send_mail(user.email, u'重置密码',
                       'auth/email/reset_password',
                       user=user, token=token,
                       next=request.args.get('next'))
        flash(u'重置密码邮件已发送到您的邮箱，请先登录系统，在登录邮箱确认重置')
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password_request.html', form=form)


# 重置密码
@auth.route('/password_reset/<token>', methods=['POST', 'GET'])
def password_reset(token):
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    form = PasswordResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            flash(u"用户不存在, 请检查用户名")
            return redirect(url_for('auth.login'))
        if user.reset_password(token=token, newpassword=form.password.data):
            flash(u"密码已经重置，请重新登录.")
        else:
            flash(u"密码重置失败,请重试")
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password.html', form=form)


# 确认邮件也要判断是否是登录状态，这样能有效避免跨站确认
@auth.route('/confirm/<token>')
def confirm(token):
    if not current_user.is_authenticated:
        flash(u"请先登录系统，再登录邮箱确认邮件")
        return redirect(url_for('auth.login'))
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash(u'您的账户已确认，谢谢！')
    else:
        flash(u'确认链接无效或者超时')
    return redirect(url_for('main.index'))


# 需要留着因为邮件确认之后刷新会用到
@auth.route('/unconfirmed')
def unconfirmed():
    if not current_user.is_anonymous and current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')


# 这里发送确认邮件的时候需要登录的
@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_mail(current_user.email, u'确认账户',
               'auth/email/confirm', user=current_user, token=token)
    flash(u'确认邮件已经发送至您的邮箱, 请确认后刷新页面重试')
    return render_template('auth/unconfirmed.html')

