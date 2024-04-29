#!/usr/bin/python3
"""
a script that is safe from sql injection
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    q = "SELECT * FROM `states` WHERE BINARY `name` = %s"
    c.execute(q, (sys.argv[4],))
    rows = c.fetchall()
    for row in rows:
        print(row)
