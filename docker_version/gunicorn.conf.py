#!/usr/bin/python3
# -*- coding: utf8 -*-

"""
filename:gunicorn.conf.py
version: docker_verison
author:elegance
"""

workers = 2    
worker_class = "gevent"   
bind = "0.0.0.0:5000"