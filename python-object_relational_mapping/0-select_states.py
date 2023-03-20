#!/usr/bin/python3
""" script that lists all states from the database """
import MySQLdb
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """Connect to MySQL database"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
        )
    """Create a cursor object"""
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    """ Fetch all the rows and print them one by one """
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
