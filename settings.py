# -*- coding: utf-8 -*-
"""
@author:韩先钊
@file: settings.py
@time: 2021/1/9  14:30
"""

class Config(object):
    DEBUG = True
    SECRET_KEY = "qwertyuiosdfghj"


class ProductionConfig(object):
    DEBUG = True


class DevelopmentConfig(object):
    DEBUG = True
    SECRET_KEY = "qwertyuiosdfghj"
    WX_GET_OPENID_PATH = "https://api.weixin.qq.com/sns/jscode2session?appid=APPID&secret=SECRET&js_code=JSCODE&grant_type=authorization_code"
    WX_APPID = "wx9e77f1caf02ba15c"
    WX_SECRET_KEY = "a5473ef14e9029751d9a940b91cccbbe"



class TestingConfig(object):
    Testing = True
