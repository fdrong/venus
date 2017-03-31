#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2017/3/24'
"""
import datetime
from app import db


class Role(db.Model):
    """
        role model
    """
    __tablename__ = 'venus_role'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(200), nullable=True)

    create_at = db.Column(db.DateTime(
        timezone=False), default=datetime.datetime.now
    )
    update_at = db.Column(db.DateTime(
        timezone=False), onupdate=datetime.datetime.now, default=datetime.datetime.now
    )

    users = db.relationship('User', secondary="venus_user_role", lazy='dynamic',
                         backref=db.backref('role', uselist=False))

    permissions = db.relationship('Permission', secondary='venus_role_permission', lazy='dynamic',
                               backref=db.backref('roles', uselist=True))

    @property
    def as_dict(self):
        """
            object to dict
        """
        return {
            db.Column.name: str(getattr(self, db.Column.name))
            for db.Column in self.__table__.db.Columns
        }

    def insert_roles(self):
        pass