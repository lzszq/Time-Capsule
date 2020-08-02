#!/usr/bin/python3
# -*- coding: utf8 -*-

"""
filename:send_email.py
version: 0.5
author:elegance
"""

from e_mail import send_mail, make_content

def select_is_send_email():
    import mysql.connector
    from get_time import compare_time
    conn = mysql.connector.connect(user = 'TimeCapsule', password = 'Time', database = 'TimeCapsule')
    cursor = conn.cursor()

    cursor.execute('select `key` from `Capsule` where `is_send_email` = 0;')
    keys = cursor.fetchall()
    user = []
    for (key,) in keys:
        cursor.execute("select DATE_FORMAT(time, '%Y-%m-%d %H:%m:%S') from `Capsule` where `key` = %s;", (key,))
        (time,) = cursor.fetchone()
        if compare_time(time):
            user.append(key)
        else:
            continue 
    cursor.close()
    conn.close()

    return user

keys = select_is_send_email()

with open(file = './privilege_key.txt', mode = 'r', encoding = 'utf8')as f:
    mail = eval(f.readline())
    f.close()

for key in keys:
    content = make_content(key, 'http://timecapsule.lizesen.xyz/open/')
    send_mail(mail_host = mail['mail_host'], mail_user = mail['mail_user'], mail_pass = mail['mail_pass'], key = key, title = 'TimeCapsule', content = content)


