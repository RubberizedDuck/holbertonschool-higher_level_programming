#!/usr/bin/python3
"""
This module is designed to print the cities of the states inputted
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    dbConnect = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                passwd=argv[2], db=argv[3])
    states_arg = argv[4]
    cur = dbConnect.cursor()
    cur.execute(
        f"SELECT cities.name FROM cities\
        INNER JOIN states ON cities.state_id = states.id\
        WHERE states.name = %(states_arg)s\
        ORDER BY cities.id", {'states_arg': states_arg})
    query_res = cur.fetchall()
    print(', '.join(row[0] for row in query_res))
