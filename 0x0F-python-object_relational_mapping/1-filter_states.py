#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa with a name starting with N
"""

import MySQLdb
import sys


if __name__ == '__main__':
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8"
            )
        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
            )
        rows = cursor.fetchall()
        for row in rows:
            if row[1][0] == 'N':
                print(row)
        cursor.close()
        db.close()
    except Exception as e:
        print("Error: {}".format(e))
