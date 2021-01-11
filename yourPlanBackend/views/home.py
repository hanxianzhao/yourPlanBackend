# -*- coding: utf-8 -*-
"""
@author:韩先钊
@file: index.py
@time: 2021/1/9  14:31
"""
import requests

from flask import Blueprint, render_template, request, session, redirect
from uuid import uuid4


home = Blueprint('home', __name__)


@home.route('/index')
def index():
    user_info = session.get('user_info')
    print(user_info)
    return 'index'


@home.route('/test')
def test():
    return 'test'

