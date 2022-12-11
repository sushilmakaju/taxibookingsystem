import mysql.connector
import sys
from backend.connector import connect

def customer_login(custInfo):
    conn=None
    sql="""SELECT * FROM customers WHERE username=%s and password=%s"""
    values=(custInfo.getusername(), custInfo.getpassword())
    result=None
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        result=cursor.fetchone()
        cursor.close()
        conn.close()


    except:
        print("Error",sys.exc_info())

    finally:
        del values, sql, conn
        return result