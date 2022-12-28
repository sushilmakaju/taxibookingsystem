from tkinter import *

from PIL import ImageTk, Image

from ui import Login_Gui


class welcome():
    def __init__(self,root):
        self.root = root
        self.root.title("Taxi booking System")
        self.root.state('zoomed')



        image = Image.open("C:\\Users\\Asus\\Desktop\\taxi-booking.png")
        image = image.resize((1290, 660))
        image = ImageTk.PhotoImage(image)
        Image_Label = Label(self.root, image=image)
        Image_Label.image = image
        Image_Label.pack(side=RIGHT, fill=BOTH, expand=True)

        lbl_heading = Label(self.root, text="Welcome to Taxi Booking System", font=("Times New Roman", 20), bg="#E5CCFF",fg="black", anchor="c", padx=20)
        lbl_heading.place(x=0, y=0, relwidth=1, height=60)


        def login():
            ##self.root.destroy()
            root = Tk()
            Login_Gui.Login(root)
            root.mainloop()

        login_btn = Button(self.root, text="login", command=login, font=("Times New Roman", 15, "bold"),bg="#E5CCFF", fg="white")
        login_btn.place(x=1150, y=10)


if __name__ == '__main__':
    root = Tk()
    welcome(root)
    root.mainloop()