#!/usr/bin/env python
import pymysql

connection = pymysql.connect(host='db', user='craft', password='qLGockJ6G2J75O', cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        while True:
            sql = input('sql> ')
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
finally:
    connection.close()
