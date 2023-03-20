#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument, safe from MySQL injections
"""
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
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
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    """Fetch all results and print them"""
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()
