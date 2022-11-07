#!/usr/bin/python3
"""
This module is designed to list all cities in the states
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    dbConnect = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                passwd=argv[2], db=argv[3])
    cur = dbConnect.cursor()
    cur.execute(
        f"SELECT cities.id, cities.name, states.name\
        FROM cities INNER JOIN states\
        ON cities.state_id = states.id\
        ORDER BY cities.id")
    query_res = cur.fetchall()
    for row in query_res:
        print(row)
