import tkinter
from tkinter import *
from tkinter import ttk


class assignbooking:
    def __init__(self,assign):
       self.assign=assign
       self.assign.title("AssignRider")
       self.assign.geometry("1000x500")
       self.assign.resizable(0,False)

       #### pannel ####
       lbl_heading = Label(self.assign, text="AssignRider", font=("Times New Roman", 20), bg="#ffff00",fg="black", anchor="c", padx=20).place(x=0, y=0, relwidth=1, height=60)

       # -------------frame------------------
       frame = LabelFrame(self.assign, font=("goudy old style", 12, "bold"), bd=2, bg="white")
       frame.place(x=110, y=70, width=720, height=60)

       #____________Label______________
       customer_lbl = Label(frame, text="Customer", font=("TimesNewRoman",15),bg="white").place(x=12,y=15)
       Rider_lbl = Label(frame, text="AssignRider", font=("TimesNewRoman",15),bg="white").place(x=320,y=15)

    #____________combobox_________

       customer_cmb = ttk.Combobox(frame,state="readonly",justify=CENTER,font=("TimesNewRoman",10))
       customer_cmb.place(x=105,y=15,width=150,height=30)

       Rider_cmb = ttk.Combobox(frame, state="readonly", justify=CENTER, font=("TimesNewRoman", 10))
       Rider_cmb.place(x=430, y=15, width=150, height=30)

    #__________button_____________
       assign_btn = Button(frame,text="Assign",font=("TimesNewRoman",15),bg="olive",fg="white").place(x=600,y=15,height=25)


    #_________________labelframe_________________________
       booked_frame = LabelFrame(self.assign, font=("TimesNewRoman", 12, "bold"), bd=2, bg="white")
       booked_frame.place(x=20, y=170, width=510, height=300)

       confirm_frame = LabelFrame(self.assign, font=("TimesNewRoman", 12, "bold"), bd=2, bg="white")
       confirm_frame.place(x=530, y=170, width=510, height=300)

        #____________label_______

       unconfirmed_lbl = Label(booked_frame, text="Unconfirmed Booking List", font=("TimesNewRoman", 15),bg="#800000", fg="white")
       unconfirmed_lbl.pack(side=TOP, fill=X)
       confirmed_lbl = Label(confirm_frame, text="Confirmed Booking List", font=("TimesNewRoman", 15), bg="#008080",fg="white").pack(side=TOP, fill=X)



if __name__ == "__main__":
    assign = Tk()
    assignbooking(assign)
    assign.mainloop()






