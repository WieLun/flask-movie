#!/usr/bin/env python
# coding:utf-8
"""
 Name: __init__.py
 Author: WieLun
 Time: 2021/1/3
 Descript:

 """

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
x = 1
# 解决跨域
cors = CORS()
cors.init_app(app=app, resources={r"/api/*": {"origins": "*"}})

app.config.from_object('config')


from app.admin import index, login, tag

for blueprint in [index, login, tag]:
    app.register_blueprint(blueprint, url_prefix='/api/v2/admin')
