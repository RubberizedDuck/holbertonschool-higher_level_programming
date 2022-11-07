#!/usr/bin/python3
"""
This module is designed to filter states by 'N'
"""

import MySQLdb
import sys

if __name__ == "__main__":
    dbConnect = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                                passwd=sys.argv[2], db=sys.argv[3])
    cur = dbConnect.cursor()
    cur.execute(
        "SELECT * FROM states\
        WHERE name LIKE BINARY 'N%'\
        ORDER BY id ASC")
    query_res = cur.fetchall()
    for row in query_res:
        print(row)
