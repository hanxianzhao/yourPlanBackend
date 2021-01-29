# -*- coding: utf-8 -*-
"""
@author:韩先钊
@file: __init__.py
@time: 2021/1/17  13:15
"""
from .home import home
from .account import account
from .login import login
from .plan import plan

# 路由配置，是否需要default
DEFAULT_BLUEPRINT = (
    (home, ''),
    (account, ''),
    (login, ''),
    (plan, '')
)


# 封装配置蓝本的函数
def config_blueprint(app):
    # 循环读取元组中的蓝本
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)
