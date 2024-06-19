#!/usr/bin/python3
import MySQLdb
import sys

db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
cur = db.cursor()

cur.execute("SELECT states.id, states.name FROM states ORDER BY id ASC")
for i in cur:
    print(i)