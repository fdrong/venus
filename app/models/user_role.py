#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2017/3/25'
"""
import datetime
from app import db


class UserRole(db.Model):
    """
        user_role model
    """
    __tablename__ = 'venus_user_role'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    user_id = db.Column(db.Integer, db.ForeignKey('venus_user.id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('venus_role.id'), nullable=False)

    create_at = db.Column(db.DateTime(
        timezone=False), default=datetime.datetime.now
    )

    @property
    def as_dict(self):
        """
            object to dict
        """
        return {
            db.Column.name: str(getattr(self, db.Column.name))
            for db.Column in self.__table__.db.Columns
        }