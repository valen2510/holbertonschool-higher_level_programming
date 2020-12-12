#!/usr/bin/python3
""" lists all cities of that state, using the database hbtn_0e_4_usa.
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities RIGHT JOIN states ON \
                states.id=cities.state_id WHERE states.name = %s", (argv[4], ))
    row = cur.fetchall()
    for city in row:
        if city is row[-1]:
            print(city[0])
        else:
            print(city[0], end=", ")
    cur.close()
    db.close()