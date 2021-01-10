# -*- coding: utf-8 -*-
"""
@author:韩先钊
@file: __init__.py
@time: 2021/1/9  14:22
"""

from flask import Flask
from .views import account, home


def create_app():
    app = Flask(__name__)
    app.config.from_object("settings.DevelopmentConfig")
    app.register_blueprint(account.account)
    app.register_blueprint(home.home)
    return app
