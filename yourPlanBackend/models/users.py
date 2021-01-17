# -*- coding: utf-8 -*-
"""
@author:韩先钊
@file: users.py
@time: 2021/1/17  13:37
"""
from datetime import datetime
from flask import current_app as app
from flask import flash
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from yourPlanBackend.extensions import db, login_manager
# from flask_login import UserMixin


# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# import pymysql
# pymysql.install_as_MySQLdb()
# app = Flask(__name__)
# app.config.from_object("settings.DevelopmentConfig")
# db = SQLAlchemy(app)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:0819@127.0.0.1:3306/test_sqlalchemy"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# from .post import Post

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    openid = db.Column(db.String(30), default="", unique=True)
    nickname = db.Column(db.String(100), default="")
    avatarurl = db.Column(db.String(100), default="")
    gender = db.Column(db.Integer, default=0)
    country = db.Column(db.String(100), default="")
    province = db.Column(db.String(100), default="")
    city = db.Column(db.String(100), default="")
    language = db.Column(db.String(100), default="")
    ctime = db.Column(db.DateTime, default=datetime.utcnow)
    mobile = db.Column(db.String(50), default="")

    def __repr__(self):
        return self.openid


    # 生成激活的token
    def generate_activate_token(self):
        # 创建用于生成token的类，需要传递秘钥和有效期expires_in默认=3600,expires_in=60
        s = Serializer(app.config['SECRET_KEY'])
        # 生成包含有效信息(必须是字典数据)的token字符串
        return s.dumps({'id': self.id})

    # 生成任意的token
    @staticmethod
    def generate_token(dict):
        s = Serializer(app.config['SECRET_KEY'])
        # 生成包含有效信息(必须是字典数据)的token字符串
        return s.dumps(dict)

    # 检查任意token是否有效,返回真实词典数据
    @staticmethod
    def check_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            flash('邮件已过期')
            return False
        except BadSignature:
            flash('无效的验证邮箱')
            return False
        return data
