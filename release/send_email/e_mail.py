#!/usr/bin/python3
# -*- coding: utf8 -*-

"""
filename:e-mail.py
version: 0.5
author:elegance
"""

def send_mail(mail_host = '', mail_user = '', mail_pass = '', key = '', title = '', content = ''):
    from get_time import get_time_now
    import smtplib 
    from email.header import Header 
    from email.mime.text import MIMEText 

    import mysql.connector

    conn = mysql.connector.connect(user = 'TimeCapsule', password = 'Time', database = 'TimeCapsule')
    cursor = conn.cursor()

    cursor.execute("update `Capsule` set `is_send_email` = 1 where `key` = %s;", (key,))
    conn.commit()
    cursor.execute("select `email` from `Capsule` where `key` = %s;", (key,))
    (receiver,) = cursor.fetchone()

    cursor.close()
    conn.close()

    sender = mail_user    
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header(f"{sender}")
    message['To'] = Header(f"{receiver}")
    message['Subject'] = title 
    
    try: 
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receiver, message.as_string()) 
    except smtplib.SMTPException as e: 

        conn = mysql.connector.connect(user = 'TimeCapsule', password = 'Time', database = 'TimeCapsule')
        cursor = conn.cursor()

        cursor.execute("update `Capsule` set `is_send_email` = 0 where `key` = %s;", (key,))
        conn.commit()

        cursor.close()
        conn.close()

        time = get_time_now()
        with open(file = './log/send_error.txt', mode = 'a', encoding = 'utf8')as f:
            f.write(f'At {time}, Sending email has failed: {receiver}, {e}') 
            f.write('\n\n')
            f.close()

def make_content(key, url):
    import mysql.connector

    conn = mysql.connector.connect(user = 'TimeCapsule', password = 'Time', database = 'TimeCapsule')
    cursor = conn.cursor()

    cursor.execute("select DATE_FORMAT(time, '%Y-%m-%d %H:%m:%S') from `Capsule` where `key` = %s;", (key,))
    (time,) = cursor.fetchone()

    cursor.close()
    conn.close()

    content = f'The TimeCapsule opened at {time}, you can go to {url} to open it. And your key is {key}.'
    return content

if __name__ == '__main__':
    #send_mail()
    pass
