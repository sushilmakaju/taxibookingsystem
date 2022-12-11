from tkinter import *


class driverdashboard:
    def __init__(self,driver):
        self.driver = driver
        self.driver.geometry("1100x500")
        self.driver.title("DriverDashboard")
        self.driver.config(bg="white")

        ################pannel###############

        lbl_heading = Label(self.driver, text="DriverDashboard", font=("Times New Roman", 20,"bold"), bg="#ffff00", fg="black",anchor="c", padx=20).place(x=0, y=0, relwidth=1, height=60)

    #################labelframe1#################
        newtrip = LabelFrame(self.driver, font=("Times New Roman", 12, "bold"), bd=2, relief=SUNKEN, bg="white")
        newtrip.place(x=30, y=70, width=500, height=300)
        newtrip_headinglbl= Label(newtrip, text="New Trip",font=("Times New Roman", 12, "bold"),bg="#ff8000",fg="black").pack(side=TOP, fill=X)


    ##############labelframe2#################
        oldtrip = LabelFrame(self.driver, font=("Times New Roman", 12, "bold"), bd=2, relief=SUNKEN, bg = "white")
        oldtrip.place(x=570, y=70, width=500, height=300)
        newtrip_headinglbl = Label(oldtrip, text="Old Trip", font=("Times New Roman", 12, "bold"), bg="#ffbf00",fg="black").pack(side=TOP, fill=X)


if __name__ == '__main__':
    driver = Tk()
    driverdashboard(driver)
    driver.mainloop()



