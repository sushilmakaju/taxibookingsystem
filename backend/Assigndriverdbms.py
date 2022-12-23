from backend.connector import connect
import mysql.connector
import sys

def getcustomersall():
    conn = None
    sql = """select booking_id from booking where booking_status = 'Pending';""" #SELECT booking_id FROM booking WHERE booking_status=Pending
    result = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()


    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return result

def driversall():
    conn = None
    sql = """SELECT driver_id FROM drivers WHERE status='Available'"""
    result = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()


    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return result



def unconfirmedbooking():
    conn = None
    sql = """SELECT * FROM booking WHERE booking_status='Pending'"""
    result = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return result

def confirmedbooking():
    conn = None
    sql = """select customers.name, booking.booking_id, 
    booking.pickup_address, booking.drop_address, 
    booking.pickup_time, booking.pickup_date from booking
     left join customers on booking.customer_id = customers.customerid
      where booking.booking_status = 'Confirmed'"""
    result = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error", sys.exc_info())
    finally:
        del sql, conn
        return result

def update_assign(Info):
    sql = """UPDATE booking SET booking_status=%s, driver_id=%s WHERE booking_id=%s"""
    values=(Info.getbooking_status(), Info.getdriver_id(), Info.getbooking_id())
    updatevalue=False
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        updatevalue=True
    except:
        print("Error", sys.exc_info())
    finally:
        del sql, conn
        return updatevalue





