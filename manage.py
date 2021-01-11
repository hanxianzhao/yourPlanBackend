# -*- coding: utf-8 -*-
"""
@author:韩先钊
@file: manage.py
@time: 2021/1/9  14:33
"""

from yourPlanBackend import create_app
from flask_script import Manager

app = create_app()
manage = Manager(app)


if __name__ == '__main__':
    manage.run()