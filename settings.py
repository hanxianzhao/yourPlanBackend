# -*- coding: utf-8 -*-
"""
@author:韩先钊
@file: settings.py
@time: 2021/1/9  14:30
"""

# 配置基类
class Config(object):
    DEBUG = True
    SECRET_KEY = "qwertyuiosdfghj"
    WX_APPID = "wx9e77f1caf02ba15c"
    WX_SECRET_KEY = "a5473ef14e9029751d9a940b91cccbbe"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:0819@127.0.0.1:3306/yourplanbackenddata"

    # 数据库公用配置
    # 无警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 自动提交
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


# 生产环境配置
class ProductionConfig(Config):
    pass

# 开发环境配置
class DevelopmentConfig(Config):
    pass


# 测试环境配置
class TestingConfig(Config):
    pass