"""
filename:start.py
version: 0.1
author:elegance
"""

from flask import Flask, render_template, request

app = Flask(__name__, static_folder = "./static", template_folder = "./templates")

@app.route('/', methods = ['GET'])
def index():
    html = render_template('index.html')
    return html


@app.route('/put/', methods = ['GET', 'POST'])
def put():
    if request.method == 'GET':
        content_type = 'put'
        html = render_template('put.html', content_type = content_type)
        return html
    if request.method == 'POST':
        pass

@app.route('/open/', methods = ['GET', 'POST'])
def open():
    if request.method == 'GET': 
        html = render_template('open.html')
        return html
    if request.method == 'POST':
        pass

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)