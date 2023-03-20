#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    """Connect to MySQL server running on localhost at port 3306"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    """Create cursor object to execute queries"""
    cursor = db.cursor()
    """Execute SQL query to list all cities"""
    cursor.execute("SELECT * FROM cities ORDER BY id ASC")
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()
