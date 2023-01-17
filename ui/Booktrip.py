import tkinter
from tkinter import *
import datetime
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
from backend.bookingdbms import insert_Booking, customerbookingtable, delete_booking, update_booking
from middleware import Global
from middleware.booking_library import bookinglibs
from tkinter import ttk

from ui import Login_Gui


class booktrip_class:
    def __init__(self,trip):
        self.trip = trip
        self.trip.title("CustomerDashboard | Welcome {}".format(Global.customerAccount[1]))
        self.trip.geometry("750x550")
        self.trip.resizable(0, False)

        frame_width = 750
        frame_height = 550
        screen_width = self.trip.winfo_screenwidth()
        screen_height = self.trip.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (frame_width / 2))
        y_cordinate = int((screen_height / 2) - (frame_height / 2))
        self.trip.geometry("{}x{}+{}+{}".format(frame_width, frame_height, x_cordinate, y_cordinate))

        custID=Entry(self.trip)
        custID.insert(0, Global.customerAccount[0])
        bookID=Entry(self.trip)

        #_______label________

        lbl_heading = Label(self.trip, text= "Customer Dashboard", font= ("Times New Roman",20, "bold"),bg="#E5CCFF", fg="black", anchor="c",padx=20)
        lbl_heading.place(x=0, y=0,relwidth=1, height=50)

        def logout():
            messagebox.showinfo("TBS", "Loging out")
            self.trip.destroy()
            trip=Tk()
            Login_Gui.Login(trip)

            trip.mainloop()

        logout_btn = Button(self.trip, text="logout", command=logout, font=("Times New Roman", 15, "bold"),bg="#E5CCFF", fg="black")
        logout_btn.place(x=650, y=10)

      #____________frame________
        pickupframe = LabelFrame(self.trip, text="Booking", font=("TimesNewRoman", 12), bd=2, relief=RIDGE,bg="white")
        pickupframe.place(x=20, y=50, width=345, height=150)

        # ==============DropFrame======================
        dropframe = LabelFrame(self.trip, text="Booking", font=("TimesNewRoman", 10), bd=2, relief=RIDGE,bg="white")
        dropframe.place(x=370, y=50, width=345, height=150)


        #_____________label_______________
        PickUpDate_lbl = Label(pickupframe, text="Date: ", font=("TimesNewRoman", 15), bg="white")
        PickUpDate_lbl.place(x=10, y=5)
        address_lbl = Label(pickupframe, text="Pickup : ", font=("TimesNewRoman", 15), bg="white")
        address_lbl.place(x=10, y=60)


        droptime_lbl = Label(dropframe, text="Time: ", font=("TimesNewRoman",15),bg="white")
        droptime_lbl.place(x=10, y=5)
        dropaddress_lbl = Label(dropframe, text="Address: ", font=("TimesNewRoman",15),bg="white")
        dropaddress_lbl.place(x=10,y=60)



        #____________entryfeild____________________
        dt= datetime.date.today()
        pickupdate_txt = DateEntry(pickupframe, font=("TimesNewRoman",15),bg="white", mindate=dt)
        pickupdate_txt.place(x=110,y=5,width=120)

        pickup_txt = Entry(pickupframe, font=("TimesNewRoman", 15), bg="white")
        pickup_txt.place(x=110,y=60,width=120)


        time_txt = Entry(dropframe, font=("TimesNewRoman",15),bg="white")

        time_txt.place(x=110,y=5,width=120)

        dropaddress_txt = Entry(dropframe, font=("TimesNewRoman", 15), bg="white")
        dropaddress_txt.place(x=110, y=60, width=120)

        def insert_booking12():

            booking=bookinglibs(booking_id='',
            pickup_address=pickup_txt.get(), pickup_date=pickupdate_txt.get(), pickup_time=time_txt.get(), drop_address=dropaddress_txt.get(), customer_id=custID.get(), booking_status='Pending')

            result=insert_Booking(booking)

            if result==True:
                messagebox.showinfo("TBS","The booking is requested")
                treeview.delete(*treeview.get_children())

                bookingtable()

            else:
                messagebox.showerror("TBS","Error Occurred")

        def delete():
            ID=bookID.get()
            deleteresult= delete_booking(ID)
            if deleteresult == True:
                messagebox.showinfo("TBS", "Booking cancelled sucessfully")
                treeview.delete(*treeview.get_children())

                bookingtable()

            else:
                messagebox.showerror("TBS", "Error Occurred")
        

        def update():
            bookingidd = bookID.get()
            pickup = pickup_txt.get()
            pickuptime = time_txt.get()
            drop = dropaddress_txt.get()


            booking = bookinglibs(booking_id=bookingidd,pickup_address = pickup, pickup_time = pickuptime,drop_address = drop)
            result = update_booking(booking)
            if result == True:
                messagebox.showinfo("Customer", "The data is updated")
                treeview.delete(*treeview.get_children())

                bookingtable()
            else:
                messagebox.showerror("Customer", "Error Occurred")


        #______________button_______________
        save_btn = Button(self.trip, text="Save",command=insert_booking12, font=("TimesNewRoman",15),bg="#808000",fg="white")
        save_btn.place(x=170,y=210, height=25)

        update_btn = Button(self.trip, text="Update",command=update, font=("TimesNewRoman",15),bg="#008080",fg="white")
        update_btn.place(x=250,y=210,height=25)


        delete_btn = Button(self.trip, text="Cancel",command=delete, font=("TimesNewRoman",15),bg="#FF7F50", fg="white")
        delete_btn.place(x=350,y=210,height=25)

        def clear():
            bookID.delete(0, END)
            pickupdate_txt.delete(0, END)
            pickup_txt.delete(0, END)
            time_txt.delete(0, END)
            dropaddress_txt.delete(0, END)

        clear_btn = Button(self.trip, text="Clear",command=clear, font=("TimesNewRoman",15),bg="#B8860B", fg="white")
        clear_btn.place(x=450,y=210,height=25)

        tab=ttk.Notebook(self.trip)
        tab.pack(side=BOTTOM, fill=BOTH)

        frame1=Frame(tab)
        frame1.pack()



        tab.add(frame1, text="Booking")


        treeview=ttk.Treeview(frame1, height=13)
        treeview.pack(side=BOTTOM, fill=BOTH)

        treeview['columns']=('id','pickup','dropoff','date','time','did','status')
        treeview.column('#0', width=0, stretch=0)
        treeview.column('id', width=100, anchor=CENTER)
        treeview.column('pickup', width=100, anchor=CENTER)
        treeview.column('dropoff', width=100, anchor=CENTER)
        treeview.column('date', width=100, anchor=CENTER)
        treeview.column('time', width=100, anchor=CENTER)
        treeview.column('did', width=100, anchor=CENTER)
        treeview.column('status', width=100, anchor=CENTER)

        treeview.heading('#0', text='', anchor=CENTER)
        treeview.heading('id', text='ID', anchor=CENTER)
        treeview.heading('pickup', text='Pickup', anchor=CENTER)
        treeview.heading('dropoff', text='Dropoff', anchor=CENTER)
        treeview.heading('date', text='Date', anchor=CENTER)
        treeview.heading('time', text='Time', anchor=CENTER)
        treeview.heading('did', text='Driver ID', anchor=CENTER)
        treeview.heading('status', text='Status', anchor=CENTER)

        def bookingtable():

            booking=customerbookingtable(custID.get())

            for a in booking:
                treeview.insert(parent='', index='end', values=(a[0],a[1],a[2],a[4],a[3],a[7],a[5]))

        bookingtable()

        def getData(sushil):

            bookID.delete(0, END)
            pickupdate_txt.delete(0, END)
            pickup_txt.delete(0, END)
            time_txt.delete(0, END)
            dropaddress_txt.delete(0, END)




            selectitem=treeview.selection()[0]

            bookID.insert(0, treeview.item(selectitem)['values'][0])
            pickupdate_txt.insert(1, treeview.item(selectitem)['values'][3])
            pickup_txt.insert(2, treeview.item(selectitem)['values'][1])
            time_txt.insert(3, treeview.item(selectitem)['values'][4])
            dropaddress_txt.insert(4,treeview.item(selectitem)['values'][2])

        treeview.bind('<<TreeviewSelect>>', getData)







if __name__ == "__main__":
    trip=Tk()
    booktrip_class(trip)
    trip.mainloop()

