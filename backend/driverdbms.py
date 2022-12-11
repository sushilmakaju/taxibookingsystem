import mysql.connector
import sys
from backend.connector import connect
from middleware.driver_library import DriverLibs

def rider(driver):
    sql = """INSERT INTO drivers VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    value = (driver.getdriver_id(),driver.getname(),driver.getphone(),
             driver.getaddress(),driver.getusername(),driver.getpassword(),
             driver.getlicenseno())
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