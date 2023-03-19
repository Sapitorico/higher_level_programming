#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''commented out'''
import MySQLdb
import sys


if __name__ == '__main__':
    '''comended'''
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )


    '''comended'''
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    '''comended'''
    for state in cur.fetchall():
        print(state)
    cur.close()
    db.close()
