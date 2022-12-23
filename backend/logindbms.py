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


def driver_login(driverInfo):
    conn=None
    sql="""SELECT * FROM drivers WHERE username=%s and password=%s"""
    values=(driverInfo.getusername(), driverInfo.getpassword())
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

def admin_login(adminInfo):
    conn=None
    sql="""SELECT * FROM admin WHERE username=%s and password=%s"""
    values=(adminInfo.getusername(), adminInfo.getpassword())
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