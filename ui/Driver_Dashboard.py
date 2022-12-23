from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from backend.bookingdbms import driverupdatebooking
from backend.driverdbms import getvalueindrivernewtable, update_driver, driverbookinghistory
from middleware import Global
from middleware.booking_library import bookinglibs
from middleware.driver_library import DriverLibs


class driverdashboard:
    def __init__(self,driver):
        self.driver = driver
        self.driver.geometry("1100x500")
        self.driver.title("DriverDashboard")
        self.driver.config(bg="white")

        driverid=Entry(self.driver)
        driverid.insert(0,Global.driverAccount[0])

        bookingid=Entry(self.driver)

        ################pannel###############

        lbl_heading = Label(self.driver, text="DriverDashboard", font=("Times New Roman", 20,"bold"), bg="#ffff00", fg="black",anchor="c", padx=20)
        lbl_heading.place(x=0, y=0, relwidth=1, height=60)

    #################labelframe1#################
        newtrip = LabelFrame(self.driver, font=("Times New Roman", 12, "bold"), bd=2, relief=SUNKEN, bg="white")
        newtrip.place(x=30, y=70, width=500, height=300)
        newtrip_headinglbl= Label(newtrip, text="New Trip",font=("Times New Roman", 12, "bold"),bg="#ff8000",fg="black")
        newtrip_headinglbl.pack(side=TOP, fill=X)


    ##############labelframe2#################
        oldtrip = LabelFrame(self.driver, font=("Times New Roman", 12, "bold"), bd=2, relief=SUNKEN, bg = "white")
        oldtrip.place(x=570, y=70, width=500, height=300)
        oldtrip_headinglbl = Label(oldtrip, text="Old Trip", font=("Times New Roman", 12, "bold"), bg="#ffbf00",fg="black")
        oldtrip_headinglbl.pack(side=TOP, fill=X)

        treeview = ttk.Treeview(newtrip, height=13)
        treeview.pack(side=BOTTOM, fill=BOTH)

        treeview['columns'] = ('id','Name', 'pickup_address', 'drop_address', 'pickup_time',
                               'pickup_date')

        treeview.column('#0', width=0, stretch=0)
        treeview.column('id', width=0, stretch=0)
        treeview.column('Name', width=100, anchor=CENTER)
        treeview.column('pickup_address', width=100, anchor=CENTER)
        treeview.column('drop_address', width=100, anchor=CENTER)
        treeview.column('pickup_time', width=100, anchor=CENTER)
        treeview.column('pickup_date', width=100, anchor=CENTER)

        treeview.heading('#0', text='', anchor=CENTER)
        treeview.heading('id', text='', anchor=CENTER)
        treeview.heading('Name', text='Name', anchor=CENTER)
        treeview.heading('pickup_address', text='Pickup', anchor=CENTER)
        treeview.heading('drop_address', text='Dropoff', anchor=CENTER)
        treeview.heading('pickup_time', text='Time', anchor=CENTER)
        treeview.heading('pickup_date', text='Date', anchor=CENTER)

        def driverassignedbooking():

            newbooking=getvalueindrivernewtable(driverid.get())
            for row in newbooking:
                treeview.insert(parent='', index='end',values=(row[0], row[1], row[2], row[3], row[4],row[5]))

        driverassignedbooking()

        def getdata(a):
            bookingid.delete(0, END)

            item=treeview.selection()[0]

            bookingid.insert(0, treeview.item(item)['values'][0])

        treeview.bind('<<TreeviewSelect>>',getdata)






















        treeview1 = ttk.Treeview(oldtrip, height=13)
        treeview1.pack(side=BOTTOM, fill=BOTH)

        treeview1['columns'] = ('Name', 'pickup_address', 'drop_address', 'pickup_time',
                               'pickup_date')

        treeview1.column('#0', width=0, stretch=0)

        treeview1.column('Name', width=100, anchor=CENTER)
        treeview1.column('pickup_address', width=100, anchor=CENTER)
        treeview1.column('drop_address', width=100, anchor=CENTER)
        treeview1.column('pickup_time', width=100, anchor=CENTER)
        treeview1.column('pickup_date', width=100, anchor=CENTER)

        treeview1.heading('#0', text='', anchor=CENTER)

        treeview1.heading('Name', text='Name', anchor=CENTER)
        treeview1.heading('pickup_address', text='Pickup', anchor=CENTER)
        treeview1.heading('drop_address', text='Dropoff', anchor=CENTER)
        treeview1.heading('pickup_time', text='Time', anchor=CENTER)
        treeview1.heading('pickup_date', text='Date', anchor=CENTER)

        def historytable():

            newbooking=driverbookinghistory(driverid.get())
            for row in newbooking:
                treeview1.insert(parent='', index='end',values=(row[0], row[1], row[2], row[3], row[4]))

        historytable()



        Note_lbl = LabelFrame(self.driver, text= "Note",font=("Times New Roman", 12, "bold"), bd=2, relief=SUNKEN, bg = "white")
        Note_lbl.place(x=100,y=370, width=800, height=100 )

        notice_lbl = Label(Note_lbl, text="Press complete Button after completing the Trip",font=("Times New Roman",15,"bold"), bg="white")
        notice_lbl.place(x=50, y=15)


        def completetrip():
            id=bookingid.get()
            booking=bookinglibs(booking_status='Complete', booking_id=id)
            result=driverupdatebooking(booking)

            driver=DriverLibs(driver_id=driverid.get(), status='Available')
            update=update_driver(driver)
            if result==True:
                messagebox.showinfo("TBS","The trip is completed")
                treeview.delete(*treeview.get_children())
                treeview1.delete(*treeview1.get_children())
                historytable()
                driverassignedbooking()

            else:
                messagebox.showerror("TBS","Error")




        complete_btn = Button(Note_lbl,command=completetrip, text="Complete", font=("Times New Roman", 12, "bold"), bg="white")
        complete_btn.place(x=650, y=15)


if __name__ == '__main__':
    driver = Tk()
    driverdashboard(driver)
    driver.mainloop()



