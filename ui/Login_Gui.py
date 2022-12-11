from tkinter import *
import tkinter as tk
import Driver_Dashboard


#from Registraion import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox

class Login:
    def __init__(self):
        self.root = Tk()
        self.user_var = tk.StringVar()
        self.pass_var = tk.StringVar()
        self.root.title("Loginpage")
        self.root.resizable(0,False)
        self.root.geometry("850x500")
        self.root.config(bg="#ffff00")

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
        lbl_usertype = Label(login_frame,text="Usertype: ", font=("TimesNewRoman",15),bg="white").place(x=32, y=165)

        #textfeild##

        username_txt = Entry(login_frame,textvariable=self.user_var,font=("Andalus",10),bg="white")
        username_txt.place(x=150, y=65, width=200, height=25)
        pass_txt = Entry(login_frame,show="*",textvariable=self.pass_var,font=("Andalus",10),bg="white")
        pass_txt.place(x=150,y=115,width=200,height=25)

        #combobox
        usertype_cmb = ttk.Combobox(login_frame,values=("Select UserType","Customer","Rider","Admin"),state='readonly',font=("TimesNewRoman",10))
        usertype_cmb.place(x=150, y=165, width=200, height=25)

        def login():
            variable12 = middleware(username=username_txt.get(), password=pass_txt.get())
            result1 = selectlogin(variable12)
            if result1 != None:
                print(result1)
                self.root.destroy()
                Driver_Dashboard(self.root)
                self.root.mainloop()


      #_______________button____________
        login_btn = Button(login_frame,text="Login", font=("italic",10),bg="white",command=login).place(x=110, y=220)
        Close_btn = Button(login_frame, text="Close", font=("italic", 10), bg="white", command=self.root.destroy).place(x=160, y=220)
        create_btn= Button(login_frame,text="Create new account", font=("italic",10),bg="white",command=self.reg).place(x=100,y=270)

        self.root.mainloop()
    ##passing default value


    def reg(self):

        self.root.withdraw()
        Registraion.registration_class(self.root)
        # self.new_win=Toplevel(self.root)
        # self.root.withdraw()
        # self.new_obj=registration_class(self.new_win)

if __name__ == "__main__":
    import Registraion

    lgn = Login()









