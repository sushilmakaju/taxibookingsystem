import tkinter
from tkinter import *
# from Login_Gui import *
from tkinter import ttk
import Login_Gui
from backend.customerdbms import customer
from middleware.customer_library import CustomerLibs
from tkinter import messagebox


class registration_class():

    def __init__(self, root):

        self.root = root
        self.root.title("Registrationpage")
        self.root.resizable(width=0, height=0)
        self.root.geometry("750x450")
        #-------------frame------------------
        frame = LabelFrame(self.root, font=("goudy old style", 12, "bold"), bd=2, relief=RIDGE, bg="white")
        frame.place(x=10, y=10, width=720, height=420)

        title = Label(frame, text="Customer Registration", font=("goudy old style", 20), bg="#ffff00", fg="black").place(x=30, y=20, width=660)

        #-----------labels-----------
        name_lbl = Label(frame, text="Name: ", font=("goudy old style", 15), bg="white").place(x=32, y=80)
        username_lbl = Label(frame, text="Username: ", font=("goudy old style", 15), bg="white").place(x=390, y=80)
        phone_lbl= Label(frame, text="Phone: ", font=("goudy old style", 15), bg="white").place(x=32, y=150)
        pass_lbl = Label(frame, text="Password: ", font=("goudy old style", 15), bg="white").place(x=390, y=150)
        Address_lbl = Label(frame, text="Address: ", font=("goudy old style",15), bg = "white").place(x=32, y=220)
        gender_lbl = Label(frame, text="Gender: ", font=("goudy old style", 15), bg="white").place(x=390, y=220)

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


        comboData=('Male','Female')
        genderCombo = ttk.Combobox(frame,values=comboData, font=("Times New Roman", 15), width=15)
        genderCombo.insert(0,'Male')
        genderCombo.place(x=500, y=220)

        def reg12():
            name1= nametxt.get()
            user= username_entry1.get()
            number=telephone_entry1.get()
            password=password_entry1.get()
            add= Address_entry1.get()
            gen=genderCombo.get()

            cus=CustomerLibs('',name=name1,phone=number,address=add,username=user,password=password,gender=gen)
            result=customer(cus)
            if result==True:
                messagebox.showinfo("TaxiBookingSystem","Customer Registered suscessfully")
            else:
                messagebox.showerror("TaxiBookingSystem","Error Registering Customer")
        def back12():
            self.root.destroy()
            root=Tk()
            Login_Gui.Login(root)
            root.mainloop()


        #_________Button_________
        Register_btn = Button(frame, text="Sumbit",font=("goudy old style",15),command=reg12, bg="#ffff00",fg="black")
        Register_btn.place(x=350,y=300,width=110,height=40)

        back_btn = Button(frame, text="Back to login",command=back12,font=("goudy old style",15), bg="#ffff00",fg="black",)
        back_btn.place(x=550,y=300,width=110,height=40)





if __name__ == "__main__":
    root=Tk()
    registration_class(root)
    root.mainloop()








