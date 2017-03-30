#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2017/3/25'
"""
import datetime
from app import db


class RolePermission(db.Model):
    """
        role_permission model
    """
    __tablename__ = 'venus_role_permission'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    role_id = db.Column(db.Integer, db.ForeignKey('venus_role.id'), nullable=False)
    permission_id = db.Column(db.Integer, db.ForeignKey('venus_permission.id'), nullable=False)

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