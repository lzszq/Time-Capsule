#!/usr/bin/python3
# -*- coding: utf8 -*-

"""
filename:gunicorn.conf.py
version: 0.3
author:elegance
"""

workers = 2    
worker_class = "gevent"   
bind = "127.0.0.1:5000"