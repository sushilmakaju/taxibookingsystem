import mysql.connector
import sys
from backend.connector import connect
from middleware.customer_library import CustomerLibs

def customer(customer):
    sql = """INSERT INTO customers VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    value = (customer.getcustomerid(),customer.getname(),customer.getphone(),
             customer.getaddress(),customer.getusername(),customer.getpassword(),
             customer.getgender())
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