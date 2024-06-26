#!/usr/bin/python3
"""script that takes in arguments and displays all values in the\\
    states table of hbtn_0e_0_usa where name matches the argument"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    state_name_searched = sys.argv[4]
    cur = db.cursor()

    cur.execute("SELECT states.id, states.name FROM states WHERE\
                states.name=%s ORDER BY states.id\
                ASC", (state_name_searched,))
    for i in cur:
        print(i)
