#!/usr/bin/env python
# coding:utf-8
"""
 Name: view.py
 Author: WieLun
 Time: 2021/1/4
 Descript:

 """
from . import tag

import json
from flask import jsonify, request
from app.utils.db_helper import SQLHelper
from app.utils.time_format import time_stamp

router = tag.route


@router('/tag/add', methods=['POST'])
def tag_add():
    data = json.loads(request.data)

    name = data['name']
    time = time_stamp()
    sql = "select * from tag where name='%s'" % (name)
    res = SQLHelper.fetch_one(sql)
    if res is not None:
        return jsonify({'status': -1, 'data': '标签%s已存在' % (name)})
    if res == -1:
        return jsonify({'status': -1, 'data': '数据库连接失败'})
    sql = "insert into tag (name,addtime) values('%s', '%s')" % (name, time)
    res = SQLHelper.execute(sql)
    if res == -1:
        return jsonify({'status': -1, 'data': '数据插入失败'})
    return jsonify({'status': 0, 'data': '标签添加成功'})


@router('/tag/list', methods=['GET'])
def tag_list():
    current_page = int(request.args['id'])
    page = int(request.args['page'])
    name = request.args['name']
    current_page = page * (current_page - 1)

    if name == '':
        sql = "select count(*) from tag"
    else:
        sql = "select count(*) from tag where name like '%%{}%%'".format(name)
    total_page = SQLHelper.fetch_one(sql)
    if total_page == -1:
        data = {'tagInfo': [], 'totalPage': 0}
        return jsonify({'status': 0, 'data': data})
    else:
        total_page = total_page[0]

    if name == '':
        sql = "select * from tag limit %d,%d" % (current_page, page)
    else:
        sql = "select * from tag where name like '%%{}%%' limit {},{}".format(name, current_page, page)
    res = SQLHelper.fetch_all(sql)
    if res == -1:
        res = []

    data = {'tagInfo': res, 'totalPage': total_page}
    return jsonify({'status': 0, 'data': data})


@router('/tag/edit', methods=['GET'])
def tag_edit():
    oldTagName = request.args['oldTagName']
    newTagName = request.args['newTagName']
    sql = "select * from tag where name='%s'" % (newTagName)
    res = SQLHelper.fetch_one(sql)
    if res is not None:
        return jsonify({'status': -1, 'data': '标签%s已存在' % (newTagName)})
    if res == -1:
        return jsonify({'status': -1, 'data': '数据库连接失败'})

    sql = "update tag set name='%s' where name='%s'" % (newTagName, oldTagName)
    res = SQLHelper.execute(sql)
    if res == -1:
        return jsonify({'status': -1, 'data': '数据插入失败'})
    return jsonify({'status': 0, 'data': "Tag修改成功"})


@router('/tag/del', methods=['GET'])
def tag_del():
    name = request.args['name']

    sql = "delete from tag where name='%s'" % (name)
    res = SQLHelper.execute(sql)
    if res == -1:
        return jsonify({'status': -1, 'data': 'tag删除失败'})
    return jsonify({'status': 0, 'data': "%s已删除" % (name)})
