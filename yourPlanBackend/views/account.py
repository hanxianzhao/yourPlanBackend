# -*- coding: utf-8 -*-
"""
@author:韩先钊
@file: account.py
@time: 2021/1/9  14:31
"""

from flask import Blueprint, render_template, request, session, redirect
from uuid import uuid4

account = Blueprint('account', __name__)


@account.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    # print(request.form)
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    if user == 'xxx' and pwd == '123':
        user_uid = str(uuid4())
        session['user_info'] = {'id': user_uid, 'name': user}
        return redirect('index')
    else:
        return render_template('login.html', msg='用户名或密码错误')
