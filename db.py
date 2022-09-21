import sqlite3
import os
from config import db_filename


def getConnect():
    db_pass = os.path.join(os.getcwd(), db_filename)
    connection = sqlite3.connect(db_pass)
    return connection.cursor()


def execute_query(query: str, single: bool):
    con = getConnect()
    if single:
        result = con.execute(query).fetchone()
    else:
        result = con.execute(query).fetchall()
    con.close()

    return result
