#!/usr/bin/python3
# -*- coding: utf8 -*-

"""
filename:init_database.py
version: 0.4
author:elegance
"""

def create_tables_of_TimeCapsule():
    import mysql.connector
    conn = mysql.connector.connect(user = 'TimeCapsule', password = 'Time', database = 'TimeCapsule')
    cursor = conn.cursor()

    cursor.execute('''create table if not exists `Capsule`(
        `id` int unsigned primary key auto_increment, 
        `key` varchar(30),
        `name` varchar(50), 
        `email` varchar(30), 
        `time` datetime,  
        `content` text, 
        `tips` text
        )charset=utf8;
    ''')
    conn.commit()

    cursor.close()
    conn.close()
    return True

def put_data(data, key):
    import mysql.connector
    conn = mysql.connector.connect(user = 'TimeCapsule', password = 'Time', database = 'TimeCapsule')
    cursor = conn.cursor()

    cursor.execute('insert into `Capsule`(`key`, `name`, `email`, `time`, `content`, `tips`) values (%s, %s, %s, %s, %s, %s)', (key, data['name'], data['email'], data['time'], data['content'], data['tips']))
    conn.commit()

    cursor.close()
    conn.close()
    return True

def get_keys():
    import mysql.connector
    conn = mysql.connector.connect(user = 'TimeCapsule', password = 'Time', database = 'TimeCapsule')
    cursor = conn.cursor()

    cursor.execute('select `key` from `Capsule`;')
    keys = cursor.fetchall()

    cursor.close()
    conn.close()

    return keys

def confirm_key(key):
    flag = False
    import mysql.connector
    conn = mysql.connector.connect(user = 'TimeCapsule', password = 'Time', database = 'TimeCapsule')
    cursor = conn.cursor()

    cursor.execute('select `key` from `Capsule`;')
    keys = cursor.fetchall()
    for (i,) in keys:
        if i == key:
            flag = True
            break

    cursor.close()
    conn.close()

    return flag

def open_data(key, data_type, filled_data):
    import mysql.connector
    conn = mysql.connector.connect(user = 'TimeCapsule', password = 'Time', database = 'TimeCapsule')
    cursor = conn.cursor()
    source = []
    
    cursor.execute('select `key` from `Capsule` where `key` = %s;', (key,))
    (i,) = cursor.fetchone()
    source.append(i)
    cursor.execute("select DATE_FORMAT(time, '%Y-%m-%d %H:%m:%S') from `Capsule` where `key` = %s;", (key,))
    (i,) = cursor.fetchone()
    source.append(i)
    cursor.execute('select `name` from `Capsule` where `key` = %s;', (key,))
    (i,) = cursor.fetchone()
    source.append(i)
    cursor.execute('select `content` from `Capsule` where `key` = %s;', (key,))
    (i,) = cursor.fetchone()
    source.append(i)
 
    for i, result in enumerate(data_type):
        filled_data[f'{result}'] = source[i]

    cursor.close()
    conn.close()

    return filled_data

def is_open_time(key):
    flag = False
    import mysql.connector
    from get_time import compare_time
    conn = mysql.connector.connect(user = 'TimeCapsule', password = 'Time', database = 'TimeCapsule')
    cursor = conn.cursor()

    cursor.execute("select DATE_FORMAT(time, '%Y-%m-%d %H:%m:%S') from `Capsule` where `key` = %s;", (key,))
    (past_time,) = cursor.fetchone()
    
    if compare_time(past_time):
        flag = True

    cursor.close()
    conn.close()

    return flag

def open_data_not_yet(key, data_type, filled_data):
    filled_data = open_data(key, data_type, filled_data)

    import mysql.connector
    conn = mysql.connector.connect(user = 'TimeCapsule', password = 'Time', database = 'TimeCapsule')
    cursor = conn.cursor()

    cursor.execute('select `tips` from `Capsule` where `key` = %s;', (key,))
    (i,) = cursor.fetchone()
    filled_data['content'] = i
    
    cursor.close()
    conn.close()

    return filled_data


if __name__ == '__main__':
    pass


