from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

from ui import Registraion, Assigndriver, Login_Gui
from ui import Driver_Registration
from ui import viewbooking


class admin_dashboard():
    def __init__(self,admin):
        self.admin = admin
        self.admin.title("TBS||Admin Dashboard")
        self.admin.resizable(0,False)
        self.admin.state('zoomed')

        #heading
        lbl_heading = Label(self.admin, text="Admin Dashboard",height=2, font=("Times New Roman", 20, "bold"), bg="blue", fg="white", padx=20)
        lbl_heading.pack(side=TOP, fill=BOTH)

        # #_________images__________
        image = Image.open("C:\\Users\\Asus\\Desktop\\download2.jpg")
        image = image.resize((1280, 640))
        image = ImageTk.PhotoImage(image)
        Image_Label = Label(self.admin, image=image)
        Image_Label.image = image
        Image_Label.pack(side=RIGHT,fill=BOTH, expand=True)

        ##side frame
        menu_frame = Frame(self.admin, bd=5, bg="white")
        menu_frame.place(x=0, y=70, width=250, height=650)

        image = Image.open("C:\\Users\\Asus\\Desktop\\images.jpg")
        image = image.resize((250, 250))
        image = ImageTk.PhotoImage(image)
        Image_Label = Label(menu_frame, image=image)
        Image_Label.image = image
        Image_Label.place(x=0, y=0)

        ##menu heading
        lblmenu_heading = Label(menu_frame, text= "Menu", font=("Times New Roman", 20, "bold"), bg="#FFCCFF", fg="black", anchor="c", padx=20)
        lblmenu_heading.place(x=0, y=290, relwidth=1)

        def customer():
            root = Tk()
            Registraion.registration_class(root)
            root.mainloop()

        def driver():
            root = Tk()
            Driver_Registration.driverres_class(root)
            root.mainloop()

        def view_booking():
            root = Tk()
            viewbooking.view_class(root)
            root.mainloop()

        def assign():
            root = Tk()
            Assigndriver.assignbooking(root)
            root.mainloop()

        def back():
            messagebox.showinfo("TBS", "Loging out your profile")
            self.admin.destroy()
            root = Tk()
            Login_Gui.Login(root)
            root.mainloop()



        ##buttons

        addcustomer_btn = Button(menu_frame, text="AddCustomer",command=customer, font=("itallic", 15, "bold"),bg="#A0A0A0", fg="black")
        addcustomer_btn.place(x=0, y=345,relwidth=1,height=30)

        adddriver_btn = Button(menu_frame, text="AddDriver",command=driver, font=("itallic", 15, "bold"), bg="#A0A0A0", fg="black")
        adddriver_btn.place(x=0, y=385, relwidth=1, height=30)

        viewbooking_btn = Button(menu_frame, text="ViewBooking",command=view_booking, font=("itallic", 15, "bold"), bg="#A0A0A0", fg="black")
        viewbooking_btn.place(x=0, y=425, relwidth=1, height=30)

        assignbooking_btn = Button(menu_frame, text="AssignDriver",command=assign, font=("itallic", 15, "bold"), bg="#A0A0A0", fg="black")
        assignbooking_btn.place(x=0, y=465, relwidth=1, height=30)

        logout_btn = Button(menu_frame, text="Logout",command=back,font=("itallic", 15, "bold"), bg="#A0A0A0",fg="black")
        logout_btn.place(x=0, y=505, relwidth=1, height=30)



if __name__ == '__main__':
    admin=Tk()
    admin_dashboard(admin)
    admin.mainloop()