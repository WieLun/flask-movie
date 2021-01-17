#!/usr/bin/env python
# coding:utf-8
"""
 Name: time_format.py
 Author: WieLun
 Time: 2021/1/16
 Descript:

 """
import datetime, time


def time_stamp():
    dtime = datetime.datetime.now()
    return time.mktime(dtime.timetuple())

# def now_time():
#     time_res = datetime.datetime.utcnow().strftime('%Y-%m-%d  %H:%M:%S')
#     return time_res
