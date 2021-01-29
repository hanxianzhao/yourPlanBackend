# -*- coding: utf-8 -*-
"""
@author:韩先钊
@file: plan.py
@time: 2021/1/29  22:37
"""

import requests
from flask import Blueprint, render_template, request, session, redirect, jsonify
from flask import current_app as app
from yourPlanBackend import urls
from yourPlanBackend.models import User, Plan
from yourPlanBackend.extensions import db

plan = Blueprint('plan', __name__)


@plan.route('/addplan', methods=['POST'])
def addplan():
    # 如果访问是post 则传过来code 通过appid和secret_key 和code去查openid和session_key
    #  "content-type":"application/x-www-form-urlencoded", 把这个搞明白
    if request.method == "POST":
        print(request)
        plan_content = request.form.get('plan_content')
        plan_picker_first = request.form.get('plan_picker_first')
        plan_picker_second = request.form.get('plan_picker_second')

        # 此处要加code判断
        print(plan_content, plan_picker_first, plan_picker_second)
        return "qwewqe"
