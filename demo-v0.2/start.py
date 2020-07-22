"""
filename:start.py
version: 0.2
author:elegance
"""

from flask import Flask, render_template, request
from secret_key import get_secret_key
from get_time import get_time_now

app = Flask(__name__, static_folder = "./static", template_folder = "./templates")

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
            with open(file = './data/test_data.txt', mode = 'r', encoding = 'utf8') as f:
                source = f.readline()
                source = f.readline()
                f.close()
            while(True):
                key = get_secret_key(20)
                if key == source:
                    continue
                else:
                    break
            
            with open(file = './data/test_data.txt', mode = 'w', encoding = 'utf8') as f:
                f.write(f'{dict(rdata)}')
                f.write('\n')
                f.write(f'{key}')
                f.close()
            
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
        with open(file = './data/test_data.txt', mode = 'r', encoding = 'utf8') as f:
            source = f.readline()
            source = eval(source)
            key = f.readline()
            f.close()

        if key == request.form['key']:
            content_type = 'open_done'
            filled_data['key'] = key
            for result in data_type:
                if result == 'key':
                    continue
                filled_data[f'{result}'] = source[f'{result}']
            html = render_template('open.html', content_type = content_type, filled_data = filled_data)
            return html

        elif key != request.form['key']:
            content_type = 'open'
            filled_data['key'] = 'Not Found'
            html = render_template('open.html', content_type = content_type, filled_data = filled_data)
            return html

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)