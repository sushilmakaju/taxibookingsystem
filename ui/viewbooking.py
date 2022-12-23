from tkinter import *
from tkinter import ttk

from backend.bookingdbms import  bookingtable12
from backend.connector import connect



class view_class():
    def __init__(self,view):
        self.view = view
        self.view.title("ViewBooking")
        self.view.resizable(0,False)
        self.view.geometry("800x250")

        custID = Entry(self.view)

        treeview = ttk.Treeview(self.view, height=13)
        treeview.pack(side=BOTTOM, fill=BOTH)

        treeview['columns'] = ('booking_id', 'pickup_address', 'drop_address', 'pickup_time',
                               'pickup_date', 'booking_status', 'customer_id', 'driver_id')

        treeview.column('#0', width=0, stretch=0)
        treeview.column('booking_id', width=100, anchor=CENTER)
        treeview.column('pickup_address', width=100, anchor=CENTER)
        treeview.column('drop_address', width=100, anchor=CENTER)
        treeview.column('pickup_time', width=100, anchor=CENTER)
        treeview.column('pickup_date', width=100, anchor=CENTER)
        treeview.column('booking_status', width=100, anchor=CENTER)
        treeview.column('customer_id', width=100, anchor=CENTER)
        treeview.column('driver_id', width=100, anchor=CENTER)

        treeview.heading('#0', text='', anchor=CENTER)
        treeview.heading('booking_id', text='Booking_ID', anchor=CENTER)
        treeview.heading('pickup_address', text='Pickup', anchor=CENTER)
        treeview.heading('drop_address', text='Dropoff', anchor=CENTER)
        treeview.heading('pickup_time', text='Time', anchor=CENTER)
        treeview.heading('pickup_date', text='Date', anchor=CENTER)
        treeview.heading('booking_status', text='Status', anchor=CENTER)
        treeview.heading('customer_id', text='Cus_id', anchor=CENTER)
        treeview.heading('driver_id', text='driver_id', anchor=CENTER)

        def viewbooking():
            view = bookingtable12()

            for i in view:
                treeview.insert(parent='', index='end', values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))

        viewbooking()





if __name__ == '__main__':
    view=Tk()
    view_class(view)
    view.mainloop()
