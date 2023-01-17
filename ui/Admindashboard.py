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

        # #_________images__________

        image2 = Image.open("C:\\Users\\Asus\\Desktop\\Taxi2.png")
        image2 = image2.resize((1300, 750))
        image2 = ImageTk.PhotoImage(image2)
        Image_Label2 = Label(self.admin, image=image2)
        Image_Label2.image = image2
        Image_Label2.place(x=0, y=0)

        #heading
        lbl_heading = Label(self.admin, text="Admin Dashboard",height=2, font=("Times New Roman", 20, "bold"), bg="#E5CCFF", fg="black", padx=20)
        lbl_heading.pack(side=TOP, fill=BOTH)



        ##side frame
        menu_frame = Frame(self.admin, bd=5, bg="white")
        menu_frame.place(x=0, y=67, width=250, height=660)

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
            self.admin.destroy()
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