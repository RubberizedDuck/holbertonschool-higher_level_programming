#!/usr/bin/python3
"""
This module is designed to be safe from SQL Injections
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    dbConnect = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                passwd=argv[2], db=argv[3])
    cur = dbConnect.cursor()
    usr_input = argv[4]
    cur.execute(
        f"SELECT * FROM states\
        WHERE name = %(usr_input)s\
        ORDER BY id ASC", {'usr_input': usr_input})
    query_res = cur.fetchall()
    for row in query_res:
        print(row)
