#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2017/3/24'
"""
import datetime
from app import db


class Permission(db.Model):
    """
        permission model
    """
    __tablename__ = 'venus_permission'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(100), nullable=False)
    codename = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(200), nullable=True, default=None)

    create_at = db.Column(db.DateTime(
        timezone=False), default=datetime.datetime.now
    )
    update_at = db.Column(db.DateTime(
        timezone=False), onupdate=datetime.datetime.now, default=datetime.datetime.now
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