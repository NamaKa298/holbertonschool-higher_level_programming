#!/usr/bin/python3
"""script that lists all states with a name starting\
    with N (upper N) from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
        if len(sys.argv) != 4:
            print("Usage: ./script.py <mysql_user> <mysql_password> <database_name>")
            sys.exit(1)

    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cur = db.cursor()

    cur.execute("SELECT states.id, states.name FROM states\
                WHERE states.name LIKE 'N%' ORDER BY id ASC")
    for i in cur:
        print(i)
