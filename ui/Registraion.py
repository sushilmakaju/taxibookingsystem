import tkinter
from tkinter import *

from tkinter import ttk
import Login_Gui
from backend.customerdbms import customer
from middleware.customer_library import CustomerLibs
from tkinter import messagebox

from middleware.regex import mobvalidation, passvalidation, usernamevalidation, namevalidation


class registration_class():

    def __init__(self, root):

        self.root = root
        self.root.title("Registrationpage")
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

        title = Label(frame, text="Customer Registration", font=("goudy old style", 20), bg="#E5CCFF", fg="black").place(x=30, y=20, width=660)

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
            name1= namevalidation(nametxt.get())
            user= usernamevalidation(username_entry1.get())
            number=mobvalidation(telephone_entry1.get())
            password=passvalidation(password_entry1.get())
            add= Address_entry1.get()
            gen=genderCombo.get()

            if nametxt.get()!='':
                if username_entry1.get()!='':
                    if telephone_entry1.get()!='':
                        if password_entry1.get()!='':
                            if name1 == True:
                                if user == True:
                                    if number == True:
                                        if password == True:
                                            cus=CustomerLibs('',name=nametxt.get(),phone=telephone_entry1.get(),address=add,username=username_entry1.get(),password=password_entry1.get(),gender=gen)
                                            result=customer(cus)
                                            if result==True:
                                                messagebox.showinfo("TaxiBookingSystem","Customer Registered suscessfully")
                                            else:
                                                messagebox.showerror("TaxiBookingSystem","Error Registering Customer")
                                        else:
                                            messagebox.showerror("TBS","Invalid Password")
                                    else:
                                        messagebox.showerror("TBS","Invalid Phone Number")
                                else:
                                    messagebox.showerror("TBS","Invalid Username")
                            else:
                                messagebox.showerror("TBS","Invalid Name")
                        else:
                            messagebox.showerror('TBS', 'Password Field is Empty')
                    else:
                        messagebox.showerror('TBS', 'Telephone Number is Empty')
                else:
                    messagebox.showerror('TBS', 'Username Field is Empty')
            else:
                messagebox.showerror('TBS', 'Name Field is Empty')





        def back12():
            self.root.destroy()
            root=Tk()
            Login_Gui.Login(root)
            root.mainloop()


        #_________Button_________
        Register_btn = Button(frame, text="Sumbit",font=("goudy old style",15),command=reg12, bg="#FFCC99",fg="black")
        Register_btn.place(x=350,y=300,width=110,height=40)

        back_btn = Button(frame, text="Back to login",command=back12,font=("goudy old style",15), bg="#FFCC99",fg="black",)
        back_btn.place(x=550,y=300,width=110,height=40)





if __name__ == "__main__":
    root=Tk()
    registration_class(root)
    root.mainloop()