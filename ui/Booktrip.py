import tkinter
from tkinter import *
import datetime
from tkcalendar import Calendar, DateEntry

class booktrip_class:
    def __init__(self,trip):
        self.trip = trip
        self.trip.title("BookTrip")
        self.trip.geometry("750x450")
        self.trip.resizable(0, False)

        #_______label________

        lbl_heading = Label(self.trip, text= "Booktrip", font= ("Times New Roman",20, "bold"),bg="blue", fg="white", anchor="c",padx=20).place(x=0, y=0,relwidth=1, height=50)

      #____________frame________
        pickupframe = LabelFrame(self.trip, text="Pick-up", font=("TimesNewRoman", 12), bd=2, relief=RIDGE,bg="white")
        pickupframe.place(x=20, y=70, width=345, height=200)

        # ==============DropFrame======================
        dropframe = LabelFrame(self.trip, text="Drop", font=("TimesNewRoman", 10), bd=2, relief=RIDGE,bg="white")
        dropframe.place(x=370, y=70, width=345, height=200)


        #_____________label_______________
        PickUpDate_lbl = Label(pickupframe, text="Date: ", font=("TimesNewRoman", 15), bg="white").place(x=10, y=5)
        pickupTime_lbl = Label(pickupframe, text="Time: ", font=("TimesNewRoman", 15), bg="white").place(x=10, y=60)
        address_lbl = Label(pickupframe, text="Address: ", font=("TimesNewRoman",15), bg="white").place(x=10,y=115)

        dropdate_lbl = Label(dropframe, text="Date: ", font=("TimesNewRoman",15),bg="white").place(x=10, y=5)
        droptime_lbl = Label(dropframe, text="Time: ", font=("TimesNewRoman",15),bg="white").place(x=10,y=60)
        dropaddress_lbl = Label(dropframe, text="address: ", font=("TimesNewRoman",15),bg="white").place(x=10,y=115)



        #____________entryfeild____________________
        pickupdate_txt = DateEntry(pickupframe, font=("TimesNewRoman",15),bg="white").place(x=110,y=5,width=120)
        pickuptime_txt = Entry(pickupframe, font=("TimesNewRoman", 15), bg="white").place(x=110,y=60,width=120)
        address_txt = Entry(pickupframe,font=("TimesNewRoman", 15), bg="white").place(x=110,y =115,width=120)

        pickupdate_txt = DateEntry(dropframe, font=("TimesNewRoman",15),bg="white").place(x=110,y=5,width=120)
        drop_txt = Entry(dropframe, font=("TimesNewRoman", 15), bg="white").place(x=110, y=60, width=120)
        dropaddress_txt = Entry(dropframe, font=("TimesNewRoman", 15), bg="white").place(x=110, y=115, width=120)

        #______________button_______________
        save_btn = Button(self.trip, text="Save", font=("TimesNewRoman",15),bg="#808000",fg="white").place(x=150,y=275, height=25)
        update_btn = Button(self.trip, text="Update", font=("TimesNewRoman",15),bg="#008080",fg="white").place(x=250,y=275,height=25)
        delete_btn = Button(self.trip, text="Delete", font=("TimesNewRoman",15),bg="#FF7F50", fg="white").place(x=350,y=275,height=25)
        clear_btn = Button(self.trip, text="Clear", font=("TimesNewRoman",15),bg="#B8860B", fg="white").place(x=450,y=275,height=25)





if __name__ == "__main__":
    trip=Tk()
    booktrip_class(trip)
    trip.mainloop()

