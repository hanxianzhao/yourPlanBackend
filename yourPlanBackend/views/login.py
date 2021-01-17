# -*- coding: utf-8 -*-
"""
@author:韩先钊
@file: login.py
@time: 2021/1/10  17:46
"""


import requests
from flask import Blueprint, render_template, request, session, redirect
from flask import current_app as app
from yourPlanBackend import urls

login = Blueprint('login', __name__)


@login.route('/userid', methods=['POST'])
def userid():
    # 如果访问是post 则传过来code 通过appid和secret_key 和code去查openid和session_key
    if request.method == "POST":
        code = request.form.get('code')
        wx_appid = app.config["WX_APPID"]
        wx_secret_key = app.config["WX_SECRET_KEY"]
        wx_openid_path = urls.WX_GET_OPENID_PATH
        # 替换掉原路径中的变量
        response = requests.get(wx_openid_path.replace("APPID", wx_appid).replace("SECRET", wx_secret_key).replace("JSCODE", code))
        response_contents = (eval(response.text))
        openid = response_contents["openid"]
        session_key = response_contents["session_key"]
        # 获取到openid则需要保存到用户表

        print(openid, session_key)
    return 'test'