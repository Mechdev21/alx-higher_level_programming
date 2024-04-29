#!/usr/bin/python3
"""
Write a script that takes in the name of a state as
an argument and lists all cities of that state, using
the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = """
            SELECT `cities`.`name`
            FROM `cities`
            INNER JOIN `states`
            ON `cities`.`state_id` = `states`.`id`
            WHERE `states`.`name` = %s
            """
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(", ".join(row), end=", ")
