# -*- coding: utf-8 -*-
"""
@author:韩先钊
@file: plans.py
@time: 2021/1/28  9:11
"""

from datetime import datetime
from yourPlanBackend.extensions import db


# id
# 创建日期
# 计划对应时间 （前端还要创建时间选择器）
# 计划对应日期（直接使用时间，字段值时间和每天）
# 计划对应周（0：本周、1：下周、2：每周）
# 计划对应月（0：本月、1：下月、2、每月）
# 计划对应年（0：今年、1：每年）
# 是否已经完成 （0：未完成、1：完成）
# 完成百分比 （预留字段，暂时不用）
# 是否重要标记 （0：不重要、1：重要，暂时可做预留字段）
# userid(与用户表id相关联)

class Plan(db.Model):
    __tablename__ = 'plans'
    id = db.Column(db.Integer, primary_key=True)
    planinfo = db.Column(db.Text, nullable=False)
    # 创建时间
    ctime = db.Column(db.DateTime, default=datetime.utcnow)
    # 需要完成时间
    plantime = db.Column(db.String(20))
    # 需要完成的日期
    plandata = db.Column(db.DATE)

    planweek = db.Column(db.Enum('本周', '下周', '每周'))
    planmonth = db.Column(db.Enum('本月', '下月', '每月'))
    planyear = db.Column(db.Enum('今年', '每年'))
    whetherdone = db.Column(db.Integer, default=0)
    whetherimp = db.Column(db.Integer, default=0)
    # 外键
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return self.plandata[20:]
