import sys

import mysql.connector
def connect():
    con=None
    try:
        con=mysql.connector.connect(host='localhost',  user='root', password='', database='taxibooking')
    except:
        print("Error : ", sys.exc_info())
    finally:
        return con