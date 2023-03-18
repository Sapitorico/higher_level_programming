#!/usr/bin/python3
import MySQLdb
import sys


if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    # connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)
    # prepare a cursor object
    cursor = db.cursor()
    # execute SQL query to fetch all states that start with "N"
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    # fetch all rows
    rows = cursor.fetchall()
    # display results
    for row in rows:
        print(row)
    # close database connection
    db.close()
