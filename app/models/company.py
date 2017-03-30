#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2017/3/25'
"""
import datetime
from app import db


class Company(db.Model):
    """
        company model
    """
    __tablename__ = 'venus_company'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False, unique=True, index=True, doc=u"单位名称")
    code = db.Column(db.String(500), nullable=True,  doc=u"单位编码")
    email = db.Column(db.String(100), nullable=False, unique=True, doc=u'单位邮箱')
    telno = db.Column(db.String(20), nullable=False, doc=u"单位电话")
    address = db.Column(db.String(200), nullable=True, doc=u"单位地址")

    create_at = db.Column(db.DateTime(
        timezone=False), default=datetime.datetime.now
    )
    update_at = db.Column(db.DateTime(
        timezone=False), onupdate=datetime.datetime.now, default=datetime.datetime.now
    )

    @staticmethod
    def generate_fake(count=100):
        from sqlalchemy.exc import IntegrityError
        from random import seed
        import forgery_py

        seed()
        for i in range(count):
            c = Company(email=forgery_py.internet.email_address(),
                        name=forgery_py.name.company_name(),
                        address=forgery_py.address.street_address(),
                        code=forgery_py.address.zip_code(),
                        telno=forgery_py.address.phone())
            db.session.add(c)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()