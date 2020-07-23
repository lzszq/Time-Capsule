#!/usr/bin/python3
# -*- coding: utf8 -*-

"""
filename:get_time.py
version: 0.2
author:elegance
"""

def get_time_now():
    import datetime
    curr_time = datetime.datetime.now()
    time_str = datetime.datetime.strftime(curr_time, '%Y-%m-%d %H:%M:%S')
    return time_str

if __name__ == '__main__':
    print(get_time_now())