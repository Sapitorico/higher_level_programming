#!/usr/bin/python3
""" script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. """
import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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
    sql_query =\
        "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    params = ('%' + state_name + '%',)
    cursor.execute(sql_query, params)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
