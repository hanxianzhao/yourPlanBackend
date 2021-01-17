# -*- coding: utf-8 -*-
"""
@author:韩先钊
@file: manage.py
@time: 2021/1/9  14:33
"""

from yourPlanBackend import create_app
from flask_script import Manager
from flask_migrate import MigrateCommand
app = create_app()
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
