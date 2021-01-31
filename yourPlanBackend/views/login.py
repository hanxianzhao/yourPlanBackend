# -*- coding: utf-8 -*-
"""
@author:韩先钊
@file: login.py
@time: 2021/1/10  17:46
"""

import requests
import json
from flask import Blueprint, render_template, request, session, redirect, jsonify
from flask import current_app as app
from yourPlanBackend import urls
from yourPlanBackend.models import User
from sqlalchemy import or_
from yourPlanBackend.extensions import db
from flask_login import login_user, logout_user, current_user

login = Blueprint('login', __name__)


@login.route('/userid', methods=['POST'])
def userid():
    # 如果访问是post 则传过来code 通过appid和secret_key 和code去查openid和session_key
    if request.method == "POST":
        # 改为使用json去获取code的值
        request_param = json.loads(request.get_data(as_text=True))
        code = request_param.get('code', '')
        # code = request.form.get('code')
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
            # 方便后面直接能拿到user.id
            db.session.flush()
            db.session.commit()
        # 登陆用户，后面直接获取用户进行使用
        login_user(user)
        # 创建token , 看下remember参数是怎么用的，暂时先使用openid和session_key（暂时先不保存）后面换user.id
        #Todo 把session-key 保存到redis key使用session_key_$userid:session-key
        # 创建的token是字节型的先将其解码转换为字符串型, 暂时先不保存session key
        # user_token = User.generate_token({'openid': openid, 'session_key': session_key}).decode()
        user_token = User.generate_token({'user_id': user.id}).decode()
        return jsonify({"token": user_token})
