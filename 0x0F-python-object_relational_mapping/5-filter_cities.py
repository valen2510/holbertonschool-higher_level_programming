#!/usr/bin/python3
""" lists all cities of that state, using the database hbtn_0e_4_usa.
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cu = db.cursor()
    cu.execute("SELECT cities.name FROM cities INNER JOIN states ON states.id=\
                cities.state_id WHERE states.name LIKE BINARY %s \
                    ORDER BY cities.id", (argv[4], ))
    row = cu.fetchall()
    print(", ".join(city[0] for city in row))
    cu.close()
    db.close()
