import tkinter
from tkinter import *
# from Login_Gui import *
from tkinter import ttk
import Login_Gui
from tkinter import messagebox
from backend.driverdbms import rider
from middleware.driver_library import DriverLibs


class driverres_class():

    def __init__(self, root):

        self.root = root
        self.root.title("DriverRegistrationpage")
        self.root.resizable(width=0, height=0)
        frame_width = 750
        frame_height = 450
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (frame_width / 2))
        y_cordinate = int((screen_height / 2) - (frame_height / 2))
        self.root.geometry("{}x{}+{}+{}".format(frame_width, frame_height, x_cordinate, y_cordinate))

        #-------------frame------------------
        frame = LabelFrame(self.root, font=("goudy old style", 12, "bold"), bd=2, relief=RIDGE, bg="white")
        frame.place(x=10, y=10, width=720, height=420)

        title = Label(frame, text="Driver Registration", font=("goudy old style", 20), bg="#ffff00", fg="black").place(x=30, y=20, width=660)

        #-----------labels-----------
        name_lbl = Label(frame, text="Name: ", font=("goudy old style", 15), bg="white").place(x=32, y=80)
        username_lbl = Label(frame, text="Username: ", font=("goudy old style", 15), bg="white").place(x=390, y=80)
        phone_lbl= Label(frame, text="Phone: ", font=("goudy old style", 15), bg="white").place(x=32, y=150)
        pass_lbl = Label(frame, text="Password: ", font=("goudy old style", 15), bg="white").place(x=390, y=150)
        Address_lbl = Label(frame, text="Address: ", font=("goudy old style",15), bg = "white").place(x=32, y=220)
        licenseno_lbl = Label(frame, text="LicenseNo: ", font=("goudy old style", 15), bg="white").place(x=390, y=220)

       #_______________Entryfield___________

        nametxt = Entry(frame, font=("Times New Roman", 15), bg="gray")
        nametxt.place(x=150, y=80,width=180)
        username_entry1 = Entry(frame, font=("Times New Roman", 15), bg="gray")
        username_entry1.place(x=500,y=80,width=180)
        telephone_entry1 = Entry(frame,font=("Times New Roman", 15), bg="gray")
        telephone_entry1.place(x=150,y=150,width=180)
        password_entry1 = Entry(frame,font=("Times New Roman", 15), bg="gray")
        password_entry1.place(x=500,y=150,width=180)
        Address_entry1 = Entry(frame,font=("Times New Roman", 15), bg="gray")
        Address_entry1.place(x=150,y=220,width=180)

        Licenseno_entry1 = Entry(frame, font=("Times New Roman", 15), bg="gray")
        Licenseno_entry1.place(x=500, y=220,width=180)

        def divreg12():
            name1 = nametxt.get()
            user = username_entry1.get()
            number = telephone_entry1.get()
            password = password_entry1.get()
            add = Address_entry1.get()
            lic = Licenseno_entry1.get()

            div = DriverLibs('', name=name1, phone=number, address=add, username=user, password=password, licenseno=lic, status='Available')
            result = rider(div)
            if result == True:
                messagebox.showinfo("TaxiBookingSystem", "Driver Registered suscessfully")
            else:
                messagebox.showerror("TaxiBookingSystem", "Error Registering Driver")

        def back12():
            self.root.destroy()
            root = Tk()
            Login_Gui.Login(root)
            root.mainloop()



        #_________Button_________
        Register_btn = Button(frame, text="Sumbit",font=("goudy old style",15),command=divreg12, bg="#ffff00",fg="black")
        Register_btn.place(x=350,y=300,width=110,height=40)

        back_btn = Button(frame, text="Back to login",font=("goudy old style",15),command=back12,bg="#ffff00",fg="black",)
        back_btn.place(x=550,y=300,width=110,height=40)





if __name__ == "__main__":
    root=Tk()
    driverres_class(root)
    root.mainloop()








