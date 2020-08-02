#!/usr/bin/python3
# -*- coding: utf8 -*-

"""
filename:get_time.py
version: 0.4
author:elegance
"""

def get_time_now():
    import datetime
    curr_time = datetime.datetime.now()
    time_str = datetime.datetime.strftime(curr_time, '%Y-%m-%d %H:%M:%S')
    return time_str

def compare_time(past_time):
    import datetime
    d1 = datetime.datetime.strptime(past_time, '%Y-%m-%d %H:%M:%S')
    d2 = datetime.datetime.strptime(get_time_now(), '%Y-%m-%d %H:%M:%S')
    if d1<d2:
        return True
    else:
        return False

if __name__ == '__main__':
    print(get_time_now())
    print(get_time_now_Y_M_D())