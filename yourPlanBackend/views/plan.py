# -*- coding: utf-8 -*-
"""
@author:韩先钊
@file: plan.py
@time: 2021/1/29  22:37
"""

import requests
import json
from flask import Blueprint, render_template, request, session, redirect, jsonify
from flask import current_app as app
from yourPlanBackend import urls
from yourPlanBackend.models import User, Plan
from yourPlanBackend.extensions import db

plan = Blueprint('plan', __name__)


@plan.route('/addplan', methods=['POST'])
def addplan():
    # 如果访问是post 则传过来code 通过appid和secret_key 和code去查openid和session_key
    #  "content-type":"application/x-www-form-urlencoded", 原生form传递方式， json则是使用json传递
    if request.method == "POST":
        # 判断token,通过token来分辨用户
        token = User.check_token(request.headers.get('token', ''))
        user_id = token.get('user_id', '')
        if user_id:
            # 获取json数据，以后主要使用json方式进行传数据
            plan_info = json.loads(request.get_data(as_text=True))
            plan_content = plan_info.get('plan_content', '')
            plan_picker_first = plan_info.get('plan_picker_first', '')
            plan_picker_second = plan_info.get('plan_picker_second', '')

            new_plan = Plan()
            new_plan.planinfo = plan_content
            if plan_picker_first == '日':
                new_plan.plandata = plan_picker_second
            elif plan_picker_first == '周':
                new_plan.planweek = plan_picker_second
            elif plan_picker_first == '月':
                new_plan.planmonth = plan_picker_second
            elif plan_picker_first == '年':
                new_plan.planyear = plan_picker_second
            new_plan.users_id = user_id
            db.session.add(new_plan)
            db.session.commit()

            # 获取的是form 数据，是以表单形式进行传递，但是层级深的情况会不方便
            # plan_content = request.form.get('plan_info')
            # plan_picker_first = request.form.get('plan_picker_first')
            # plan_picker_second = request.form.get('plan_picker_second')
            # 新建成功直接返回True
            return jsonify({"response": True})
