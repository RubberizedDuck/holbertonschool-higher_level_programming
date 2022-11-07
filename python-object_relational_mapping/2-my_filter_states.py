#!/usr/bin/python3
"""
This module is designed to allow user input to filter states
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    dbConnect = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                passwd=argv[2], db=argv[3])
    cur = dbConnect.cursor()
    usr_input = argv[4]
    cur.execute(
        "SELECT * FROM states\
        WHERE name LIKE BINARY '{}'\
        ORDER BY id ASC".format(usr_input))
    query_res = cur.fetchall()
    for row in query_res:
        print(row)
