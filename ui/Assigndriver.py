import tkinter
from tkinter import *
from tkinter import ttk, messagebox

from backend.Assigndriverdbms import getcustomersall, unconfirmedbooking, confirmedbooking, update_assign
from backend.Assigndriverdbms import driversall
from backend.driverdbms import update_driver
from middleware.booking_library import bookinglibs
from middleware.driver_library import DriverLibs


class assignbooking:
    def __init__(self,assign):
       self.assign=assign
       self.assign.title("AssignRider")
       self.assign.geometry("1100x500")
       self.assign.resizable(0,False)

       #### pannel ####
       lbl_heading = Label(self.assign, text="AssignRider", font=("Times New Roman", 20), bg="#ffff00",fg="black", anchor="c", padx=20)
       lbl_heading.place(x=0, y=0, relwidth=1, height=60)

       # -------------frame------------------
       frame = LabelFrame(self.assign, font=("goudy old style", 12, "bold"), bd=2, bg="white")
       frame.place(x=110, y=70, width=720, height=60)

       #____________Label______________
       customer_lbl = Label(frame, text="Customer", font=("TimesNewRoman",15),bg="white")
       customer_lbl.place(x=12,y=15)
       Rider_lbl = Label(frame, text="AssignRider", font=("TimesNewRoman",15),bg="white")
       Rider_lbl.place(x=320,y=15)

    #____________combobox_________
       result = getcustomersall()
       data = [i for i, in result]

       customer_cmb = ttk.Combobox(frame,state="readonly", values=data,justify=CENTER,font=("TimesNewRoman",10))
       customer_cmb.place(x=105,y=15,width=150,height=30)



       def ridercombina():
            result2 = driversall()
            data2 = [a for a, in result2]

            Rider_cmb.configure(values=data2)


       Rider_cmb = ttk.Combobox(frame, state="readonly", justify=CENTER, font=("TimesNewRoman", 10))
       Rider_cmb.place(x=430, y=15, width=150, height=30)
       ridercombina()






       def Assign():
          change_confirmed = bookinglibs(booking_id=customer_cmb.get(), driver_id=Rider_cmb.get(), booking_status='Confirmed')
          updatevalue = update_assign(change_confirmed)

          driver = DriverLibs(driver_id=Rider_cmb.get(), status='Unavailable')
          update = update_driver(driver)

          if updatevalue == True:
             messagebox.showinfo("Taxi Booking", 'Booking Confirmed')
             treeview.delete(*treeview.get_children())
             treeview1.delete(*treeview1.get_children())
             unconfirmed()
             confirmed()
             Rider_cmb.delete(0, END)
             ridercombina()


          else:
             messagebox.showerror("Taxi Booking",'Error')


    #__________button_____________
       assign_btn = Button(frame,text="Assign",font=("TimesNewRoman",15),bg="olive",fg="white", command=Assign)
       assign_btn.place(x=600,y=15,height=25)


    #_________________labelframe_________________________
       booked_frame = LabelFrame(self.assign, font=("TimesNewRoman", 12, "bold"), bd=2, bg="white")
       booked_frame.place(x=20, y=170, width=510, height=300)

       confirm_frame = LabelFrame(self.assign, font=("TimesNewRoman", 12, "bold"), bd=2, bg="white")
       confirm_frame.place(x=530, y=170, width=510, height=300)

        #____________label_______

       unconfirmed_lbl = Label(booked_frame, text="Unconfirmed Booking List", font=("TimesNewRoman", 15),bg="#800000", fg="white")
       unconfirmed_lbl.pack(side=TOP, fill=X)
       confirmed_lbl = Label(confirm_frame, text="Confirmed Booking List", font=("TimesNewRoman", 15), bg="#008080",fg="white")
       confirmed_lbl.pack(side=TOP, fill=X)

       treeview = ttk.Treeview(booked_frame, height=13)
       treeview.pack(side=BOTTOM, fill=BOTH)

       treeview['columns'] = ('pickup_address', 'drop_address', 'pickup_time',
                              'pickup_date')

       treeview.column('#0', width=0, stretch=0)
       treeview.column('pickup_address', width=100, anchor=CENTER)
       treeview.column('drop_address', width=100, anchor=CENTER)
       treeview.column('pickup_time', width=100, anchor=CENTER)
       treeview.column('pickup_date', width=100, anchor=CENTER)

       treeview.heading('#0', text='', anchor=CENTER)
       treeview.heading('pickup_address', text='Pickup', anchor=CENTER)
       treeview.heading('drop_address', text='Dropoff', anchor=CENTER)
       treeview.heading('pickup_time', text='Time', anchor=CENTER)
       treeview.heading('pickup_date', text='Date', anchor=CENTER)

       treeview1 = ttk.Treeview(confirm_frame, height=13)
       treeview1.pack(side=BOTTOM, fill=BOTH)
       treeview1['columns'] = ('CustomerName','booking_id','pickup_address', 'drop_address', 'pickup_time','pickup_date')

       treeview1.column('#0', width=0, stretch=0)
       treeview1.column('CustomerName', width=100, anchor=CENTER)
       treeview1.column('booking_id', width=0, stretch=0)
       treeview1.column('pickup_address', width=100, anchor=CENTER)
       treeview1.column('drop_address', width=100, anchor=CENTER)
       treeview1.column('pickup_time', width=100, anchor=CENTER)
       treeview1.column('pickup_date', width=100, anchor=CENTER)


       treeview1.heading('#0', text='', anchor=CENTER)
       treeview1.heading('CustomerName', text='Name', anchor=CENTER)
       treeview1.heading('booking_id', text='', anchor=CENTER)
       treeview1.heading('pickup_address', text='Pickup', anchor=CENTER)
       treeview1.heading('drop_address', text='Dropoff', anchor=CENTER)
       treeview1.heading('pickup_time', text='Time', anchor=CENTER)
       treeview1.heading('pickup_date', text='Date', anchor=CENTER)

       def unconfirmed():
          unconfirm = unconfirmedbooking()

          for x in unconfirm:
             treeview.insert(parent='', index='end',values=(x[1],x[2],x[3],x[4]))
       unconfirmed()

       def confirmed():
          confirm = confirmedbooking()

          for y in confirm:
             treeview1.insert(parent='', index='end', values=(y[0],y[1],y[2],y[3],y[4],y[5]))
       confirmed()




if __name__ == "__main__":
    assign = Tk()
    assignbooking(assign)
    assign.mainloop()






