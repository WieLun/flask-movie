#!/usr/bin/env python
#coding:utf-8
"""
 Name: view.py
 Author: WieLun
 Time: 2021/1/4
 Descript:

 """
from . import index
router = index.route
@router('/add', methods=['GET'])
def index():
    return 'hello world'