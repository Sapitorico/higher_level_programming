#!/usr/bin/python3
'''sssss'''
import MySQLdb
import sys


if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)
    '''sssss'''
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    '''sssss'''
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    '''sssss'''
    db.close()
