#!/usr/bin/python3
# -*- coding: utf8 -*-

"""
filename:send_email.py
version: 0.5
author:elegance
"""

from e_mail import send_mail, make_content
from init_database import select_is_send_email

data = select_is_send_email()

with open(file = './privilege_key.txt', mode = 'r', encoding = 'utf8')as f:
    mail = eval(f.readline())
    f.close()

for user in data:
    content = make_content(user, 'http://timecapsule.lizesen.xyz/open/')
    send_mail(mail_host = mail['mail_host'], mail_user = mail['mail_user'], mail_pass = mail['mail_pass'], receiver = user, title = 'TimeCapsule', content = content)

if __name__ == '__main__':
    pass