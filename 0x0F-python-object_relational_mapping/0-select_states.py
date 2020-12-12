#!/usr/bin/python3
""" Lists all the states from a database hbtn_0e_0_usa.
"""


import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    row = cur.fetchall()
    for states in row:
        print(states)
    cur.close()
    db.close()
