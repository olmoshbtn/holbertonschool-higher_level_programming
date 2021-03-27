#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            )

        cursor = db.cursor()

        query = """
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            """

        cursor.execute(query, (argv[4], ))

        rows = cursor.fetchall()
        rows = [city[0] for city in rows]

        print(', '.join(rows))

        cursor.close()
        db.close()

    except Exception as e:
        print("Error: {}".format(e))
