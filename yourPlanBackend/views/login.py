# -*- coding: utf-8 -*-
"""
@author:韩先钊
@file: login.py
@time: 2021/1/10  17:46
"""


import requests
from flask import Blueprint, render_template, request, session, redirect
from flask import current_app as app

login = Blueprint('login', __name__)


@login.route('/userid', methods=['POST'])
def userid():
    if request.method == "POST":
        code = request.form.get('code')
        wx_appid = app.config["WX_APPID"]
        wx_secret_key = app.config["WX_SECRET_KEY"]
        wx_openid_path = app.config["WX_GET_OPENID_PATH"]
        # 替换掉原路径中的变量
        response = requests.get(wx_openid_path.replace("APPID", wx_appid).replace("SECRET", wx_secret_key).replace("JSCODE", code))
        response_contents = (eval(response.text))
        openid = response_contents["openid"]
        session_key = response_contents["session_key"]
        print(openid, session_key)
    return 'test'