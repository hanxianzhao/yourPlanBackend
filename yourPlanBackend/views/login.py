# -*- coding: utf-8 -*-
"""
@author:韩先钊
@file: login.py
@time: 2021/1/10  17:46
"""

import requests
from flask import Blueprint, render_template, request, session, redirect, jsonify
from flask import current_app as app
from yourPlanBackend import urls
from yourPlanBackend.models import User
from sqlalchemy import or_
from yourPlanBackend.extensions import db
from flask_login import login_user, logout_user, current_user
import json

login = Blueprint('login', __name__)


@login.route('/userid', methods=['POST'])
def userid():
    # 如果访问是post 则传过来code 通过appid和secret_key 和code去查openid和session_key
    if request.method == "POST":
        code = request.form.get('code')
        # 此处要加code判断
        print(code)
        wx_appid = app.config["WX_APPID"]
        wx_secret_key = app.config["WX_SECRET_KEY"]
        wx_openid_path = urls.WX_GET_OPENID_PATH
        # 替换掉原路径中的变量
        response = requests.get(
            wx_openid_path.replace("APPID", wx_appid).replace("SECRET", wx_secret_key).replace("JSCODE", code))
        response_contents = (eval(response.text))
        openid = response_contents["openid"]
        session_key = response_contents["session_key"]
        # 获取到openid则需要保存到用户表，并且通过appid和secret_key生成token
        # 获取数据，查看openid是否存在
        user = User.query.filter(User.openid == openid).first()
        if not user:
            # 创建用户
            user = User(openid=openid)
            db.session.add(user)
            db.session.commit()
        # else:
        # 创建token , 看下remember参数是怎么用的
        login_user(user)
        user_token = current_user.generate_token({'openid': openid, 'session_key': session_key})
        # user_token = current_user.generate_token({'id': user.id})
        print("user_token===", user_token)
        print(type(user_token))
        response = {"token": str(user_token)}
        # return jsonify(token=user_token)
        return jsonify(response)
        # return response
        # return user_token
