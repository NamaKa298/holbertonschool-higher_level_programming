#!/usr/bin/python3
"""script that takes in the name of a state as an argument and\\
    lists all cities of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    state_name = sys.argv[4]
    cur: MySQLdb.cursors.Cursor = db.cursor()

    cur.execute("SELECT cities.name FROM cities JOIN\
                states ON states.id = cities.state_id WHERE\
                states.name=%s ORDER BY cities.id ASC", (state_name,))

    current_count = 0

    for row in cur:
        current_count += 1
        print(row[0], end=", " if (current_count < cur.rowcount) else "\n")
