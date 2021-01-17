#!/usr/bin/env python
# coding:utf-8
"""
 Name: db_helper.py
 Author: WieLun
 Time: 2021/1/6
 Descript:

 """
from app import app
import pymysql
from DBUtils.PooledDB import PooledDB

hostname = app.config['HOSTNAME']
port = app.config['PORT']
database = app.config['DATABASE']
username = app.config['USERNAME']
password = app.config['PASSWORD']



POOL = PooledDB(
    creator=pymysql,
    maxconnections=6,
    mincached=2,
    maxcached=5,
    maxshared=3,
    blocking=True,
    maxusage=None,
    setsession=[],
    ping=0,
    # closeable=False,
    # threadlocal=None,
    host=hostname,
    port=port,
    user=username,
    password=password,
    database=database,
    charset='utf8',
)


class SQLHelper(object):
    @staticmethod
    def fetch_one(sql, *args):
        try:
            conn = POOL.connection()
            cursor = conn.cursor()
            cursor.execute(sql, args)
            res = cursor.fetchone()
            cursor.close()
            conn.close()
        except Exception as e:
            res = 400
        return res

    @staticmethod
    def fetch_all(sql, *args):
        try:
            conn = POOL.connection()
            cursor = conn.cursor()
            cursor.execute(sql, args)
            res = cursor.fetchall()
            cursor.close()
            conn.close()
        except Exception as e:
            res = 400
        return res

    @staticmethod
    def execute(sql, *args):
        try:
            conn = POOL.connection()
            cursor = conn.cursor()
            res = cursor.execute(sql, args)
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            res = 400
        return res