import mysql.connector
import sys
from backend.connector import connect
from middleware.driver_library import DriverLibs

def rider(driver):
    sql = """INSERT INTO drivers VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    value = (driver.getdriver_id(),driver.getname(),driver.getphone(),
             driver.getaddress(),driver.getusername(),driver.getpassword(),
             driver.getlicenseno(),driver.getstatus())
    result=False
    try:
        con = connect()
        cursor = con.cursor()
        cursor.execute(sql,value)
        con.commit()
        cursor.close()
        con.close()
        result=True
    except:
        print("Error : ", sys.exc_info())
    finally:
        del value,sql
        return result

def getvalueindrivernewtable(did):
    sql ="""select booking.booking_id, customers.name, booking.pickup_address, booking.drop_address, booking.pickup_time, 
    booking.pickup_date from booking inner join customers on booking.customer_id=customers.customerid 
    where booking.driver_id=%s and booking.booking_status='Confirmed'"""
    values = (did,)
    newbooking=None
    try:
        con = connect()
        cursor = con.cursor()
        cursor.execute(sql, values)
        newbooking=cursor.fetchall()
        cursor.close()
        con.close()
    except:
        print("Error :", sys.exc_info())
    finally:
        del values, sql
        return newbooking

def update_driver(did):
    sql = '''UPDATE drivers set status=%s WHERE driver_id=%s '''
    values=(did.getstatus(), did.getdriver_id())
    update = False
    try:
        con = connect()
        cursor = con.cursor()
        cursor.execute(sql, values)
        con.commit()
        cursor.close()
        con.close()
        update=True
    except:
        print("Error :", sys.exc_info())
    finally:
        del sql
        return update


def driverbookinghistory(did):
    sql ="""select customers.name, booking.pickup_address, booking.drop_address, booking.pickup_time, 
    booking.pickup_date from booking inner join customers on booking.customer_id=customers.customerid 
    where booking.driver_id=%s and booking.booking_status='Complete'"""
    values = (did,)
    newbooking=None
    try:
        con = connect()
        cursor = con.cursor()
        cursor.execute(sql, values)
        newbooking=cursor.fetchall()
        cursor.close()
        con.close()
    except:
        print("Error :", sys.exc_info())
    finally:
        del values, sql
        return newbooking




