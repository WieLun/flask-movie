#!/usr/bin/env python
#coding:utf-8
"""
 Name: view.py
 Author: WieLun
 Time: 2021/1/4
 Descript:

 """
from . import login
import json
import base64
from flask import jsonify, request
from app.utils.db_helper import SQLHelper

router = login.route

@router('/login', methods=['post'])
def login():
    # data = json.loads(request.get_data())
    data = json.loads(request.data)
    sql = "select * from user where name='%s' and password='%s';" % (data['username'], data['password'])
    res = SQLHelper.fetch_one(sql)
    if res == -1:
        return jsonify({'status': -1, 'data': '数据库查询失败'})
    if res is None:
        return jsonify({'status': -1, 'data': '账号或密码错误'})

    return jsonify({'status': 0, 'data': 'login success'})