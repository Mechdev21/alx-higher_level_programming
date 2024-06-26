#!/usr/bin/python3
"""
Write a script that lists all cities from the database
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    q = """
            SELECT *
            FROM `cities`
            INNER JOIN `states`
            ON `cities`.`state_id` = `states`.`id`
            ORDER BY `cities`.`id`
            """
    c.execute(q)
    rows = c.fetchall()
    for row in rows:
        print(row)
