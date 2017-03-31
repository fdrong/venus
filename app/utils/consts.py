#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2017/3/31'
"""

from app.models import Company
CompanyChoices = [(company.id, company.name) for company in Company.query.all()]