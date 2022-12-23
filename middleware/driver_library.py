
class DriverLibs():
    def __init__(self,driver_id=0,name=None,phone=None,address=None,username=None,password=None,licenseno=None,status=None):
        self.driver_id=driver_id
        self.name=name
        self.phone=phone
        self.address=address
        self.username=username
        self.password=password
        self.licenseno=licenseno
        self.status=status

        #getter
    def getdriver_id(self):
        return self.driver_id
    def getname(self):
        return self.name
    def getphone(self):
        return self.phone
    def getaddress(self):
        return self.address
    def getusername(self):
        return self.username
    def getpassword(self):
        return self.password
    def getlicenseno(self):
        return self.licenseno
    def getstatus(self):
        return self.status

    #setter
    def setdriver_id(self,driver_id):
        self.driver_id=driver_id
    def setname(self,name):
        self.name=name
    def setphone(self,phone):
        self.phone=phone
    def setaddress(self,address):
        self.address=address
    def setusername(self,username):
        self.username=username
    def setpassword(self,password):
        self.password=password
    def setgender(self,licenseno):
        self.licenceno=licenseno
    def setstatus(self,status):
        self.status=status

    #str/tostring
    def __str__(self):
        return("{}, {}, {}, {}, {}, {}, {}, {}".format(self.driver_id,self.name,self.phone,self.address,self.username,self.password,self.licenceno, self.status))

