# -*- coding: utf-8 -*-
"""
@author:韩先钊
@file: __init__.py
@time: 2021/1/9  14:22
"""

from flask import Flask
from .views import config_blueprint
from .extensions import config_extensions
from .models.users import User
from .models.plans import Plan

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings.DevelopmentConfig")
    # 蓝本注册
    config_blueprint(app)
    # 加载扩展
    config_extensions(app)
    return app
