from tkinter import *
import tkinter as tk
import Driver_Dashboard


#from Registraion import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox

from backend.logindbms import customer_login
from middleware import Global
from middleware.customer_library import CustomerLibs
from ui import Registraion, Booktrip


class Login():
    def __init__(self, root):
        self.root=root



        self.root.title("Loginpage")
        self.root.resizable(0,False)
        self.root.geometry("850x500")
        self.root.config(bg="#ffff00")

        self.user_var = tk.StringVar()
        self.pass_var = tk.StringVar()

        #### pannel ####
        lbl_heading = Label(self.root, text= "Taxi Booking System", font= ("Times New Roman",20, "bold"),bg="blue", fg="white", anchor="c",padx=20).place(x=0, y=0,relwidth=1, height=80)

        # #_________images__________
        self.bg_frame = Image.open("C:\\Users\\Asus\\Desktop\\river.png")
        photo = ImageTk.PhotoImage(self.bg_frame, master=self.root)
        self.bg_panel = Label(self.root, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')


        ####frame####
        login_frame = Frame(self.root,bd=5,bg="white")
        login_frame.place(x=220, y=80, width=450, height=350)

        ##labels#
        lbl_heading = Label(login_frame,text="Login here", font=("Elephant",18,"bold"),bg="white").place(x=32,y=10,relwidth=1)
        lbl_username = Label(login_frame,text="Username: ", font=("TimesNewRoman",15),bg="white").place(x=32,y=65)
        lbl_password = Label(login_frame,text="Password: ", font=("TimesNewRoman",15),bg="white").place(x=32, y=115)


        #textfeild##

        username_txt = Entry(login_frame,textvariable=self.user_var,font=("Andalus",10),bg="white")
        username_txt.place(x=150, y=65, width=200, height=25)
        pass_txt = Entry(login_frame,show="*",textvariable=self.pass_var,font=("Andalus",10),bg="white")
        pass_txt.place(x=150,y=115,width=200,height=25)



        def login():
            variable12 = CustomerLibs(username=username_txt.get(), password=pass_txt.get())
            result1 = customer_login(variable12)
            if result1 != None:
                Global.customerAccount =result1
                messagebox.showinfo("TBS",'Welcome {}'.format(username_txt.get()))
                self.root.destroy()
                root=Tk()
                Booktrip.booktrip_class(root)
                root.mainloop()

            else:
                messagebox.showerror("TBS","Error Occurred")


      #_______________button____________
        login_btn = Button(login_frame,text="Login",command=login, font=("italic",10),bg="white")
        login_btn.place(x=150, y=180)
        Close_btn = Button(login_frame, text="Close", font=("italic", 10), bg="white", command=self.root.destroy)
        Close_btn.place(x=200, y=180)


        def registration():

            self.root.destroy()
            root=Tk()
            Registraion.registration_class(root)
            root.mainloop()

        create_btn= Button(login_frame,text="Create new account",command=registration, font=("italic",10),bg="white")
        create_btn.place(x=150,y=220)

        self.root.mainloop()





if __name__ == "__main__":
    root=Tk()
    Login(root)
    root.mainloop()











