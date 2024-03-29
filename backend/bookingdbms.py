import mysql.connector
import sys
from backend.connector import connect
from middleware.booking_library import bookinglibs

def insert_Booking(booking):
    sql = """INSERT INTO booking VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    value = (booking.getbooking_id(), booking.getpickup_address(), booking.getdrop_address(),
             booking.getpickup_time(), booking.getpickup_date(), booking.getbooking_status(),
             booking.getcustomer_id(), booking.getdriver_id())
    result = False
    try:
        con = connect()
        cursor = con.cursor()
        cursor.execute(sql, value)
        con.commit()
        cursor.close()
        con.close()
        result = True
    except:
        print("Error : ", sys.exc_info())
    finally:
        del value, sql
        return result


def customerbookingtable(customerid):
    conn=None
    sql="""SELECT * FROM booking WHERE customer_id=%s"""
    values=(customerid,)
    result=None
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        result=cursor.fetchall()
        cursor.close()
        conn.close()


    except:
        print("Error", sys.exc_info())

    finally:
        del values, sql, conn
        return result

def delete_booking(delete):
    conn = None
    sql = """DELETE FROM booking WHERE booking_id=%s"""
    values = (delete,)
    deleteresult = False
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        deleteresult = True
    except:
        print("Error", sys.exc_info())
    finally:
        del values, sql, conn
        return deleteresult

def update_booking(update):
    conn = None
    sql = """UPDATE booking set pickup_address=%s, pickup_time=%s, drop_address=%s WHERE booking_id=%s"""
    values = (update.getpickup_address(), update.getpickup_time(), update.getdrop_address(), update.getbooking_id())
    updateresult = False
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        updateResult = True

    except:
        print("Error", sys.exc_info())

    finally:
        del values, sql, conn
        return updateResult

def bookingtable12():
    conn=None
    sql="""SELECT * FROM booking"""
    result=None
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        result=cursor.fetchall()
        cursor.close()
        conn.close()


    except:
        print("Error", sys.exc_info())

    finally:
        del  sql, conn
        return result


def driverupdatebooking(booking):
    conn=None
    sql="""UPDATE booking set booking_status=%s WHERE booking_id=%s"""
    values=(booking.getbooking_status(), booking.getbooking_id())
    result=False
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result=True


    except:
        print("Error", sys.exc_info())

    finally:
        del  sql, conn
        return result


