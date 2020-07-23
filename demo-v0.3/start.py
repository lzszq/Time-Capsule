#!/usr/bin/python3
# -*- coding: utf8 -*-

"""
filename:start.py
version: 0.3
author:elegance
"""

from flask import Flask, render_template, request
from secret_key import get_secret_key
from get_time import get_time_now
from init_database import create_tables_of_TimeCapsule, put_data, get_keys, confirm_key, open_data

app = Flask(__name__, static_folder = "./static", template_folder = "./templates")
create_tables_of_TimeCapsule()

@app.route('/', methods = ['GET'])
def index():
    html = render_template('index.html')
    return html


@app.route('/put/', methods = ['GET', 'POST'])
def put_capsule():
    origin_type = ('name', 'email', 'time', 'content', 'tips')
    filled_data = {result:'' for result in origin_type}
    filled_data['time'] = get_time_now()
    data_type = ('name', 'email', 'content', 'tips')
    is_filled = [False for i in range(len(data_type))]

    if request.method == 'GET':
        content_type = 'put'
        html = render_template('put.html', content_type = content_type, is_filled = is_filled, filled_data = filled_data)
        return html

    if request.method == 'POST':
        rdata = request.form
        flag = False
        for i, result in enumerate(data_type):
            filled_data[f'{result}'] = rdata[f'{result}']
            if rdata[f'{result}'] == '':
                is_filled[i] = True
                flag = True

        if flag:
            html = render_template('put.html', content_type = content_type, is_filled = is_filled, filled_data = filled_data)
            return html
            
        else:
            content_type = 'put_done'
            
            keys = get_keys()
            key = get_secret_key(20)

            for result in keys:
                if key == result:
                    key = get_secret_key(20)
            
            put_data(rdata, key)
            
            html = render_template('put.html', content_type = content_type, key = key)
            return html


@app.route('/open/', methods = ['GET', 'POST'])
def open_capsule():
    data_type = ('key', 'time', 'name', 'content')
    filled_data = {result:'' for result in data_type}

    if request.method == 'GET': 
        content_type = 'open'
        html = render_template('open.html', content_type = content_type, filled_data = filled_data)
        return html

    if request.method == 'POST':
        flag = confirm_key(request.form['key'])

        if flag:
            content_type = 'open_done'
            filled_data['key'] = request.form['key']
            filled_data = open_data(request.form['key'], data_type, filled_data)
            html = render_template('open.html', content_type = content_type, filled_data = filled_data)
            return html

        elif flag:
            content_type = 'open'
            filled_data['key'] = 'Not Found'
            html = render_template('open.html', content_type = content_type, filled_data = filled_data)
            return html

@app.route('/introduce', methods = ['GET'])
def introduce():
    html = render_template('introduce.html')
    return html

if __name__ == '__main__':
    app.run(debug = True)
