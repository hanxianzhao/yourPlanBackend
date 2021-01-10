# -*- coding: utf-8 -*-
"""
@author:韩先钊
@file: manage.py
@time: 2021/1/9  14:33
"""

from .yourPlanBackend import create_app

app = create_app()

if __name__ == '__main__':
    app.run()