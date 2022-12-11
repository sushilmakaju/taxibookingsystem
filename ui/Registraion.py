import tkinter
from tkinter import *
# from Login_Gui import *
from tkinter import ttk
import Login_Gui

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

        name_entry = Entry(frame, font=("Times New Roman", 15), bg="gray").place(x=150, y=80,width=180)
        username_entry = Entry(frame, font=("Times New Roman", 15), bg="gray").place(x=500,y=80,width=180)
        telephone_entry = Entry(frame,font=("Times New Roman", 15), bg="gray").place(x=150,y=150,width=180)
        password_entry = Entry(frame,font=("Times New Roman", 15), bg="gray").place(x=500,y=150,width=180)
        Address_entry = Entry(frame,font=("Times New Roman", 15), bg="gray").place(x=150,y=220,width=180)


        comboData=('Male','Female')
        genderCombo = ttk.Combobox(frame,values=comboData, font=("Times New Roman", 15), width=15)
        genderCombo.insert(0,'Male')
        genderCombo.place(x=500, y=220)


        #_________Button_________
        Register_btn = Button(frame, text="Sumbit",font=("goudy old style",15), bg="#ffff00",fg="black").place(x=350,y=300,width=110,height=40)
        back_btn = Button(frame, text="Back to login",font=("goudy old style",15), bg="#ffff00",fg="black",)
        back_btn.place(x=550,y=300,width=110,height=40)





if __name__ == "__main__":
    root=Tk()
    registration_class(root)
    root.mainloop()








