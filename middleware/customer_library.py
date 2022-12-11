
class CustomerLibs():
    def __init__(self,customerid=0,name=None,phone=None,address=None,username=None,password=None,gender=None):
        self.customerid=customerid
        self.name=name
        self.phone=phone
        self.address=address
        self.username=username
        self.password=password
        self.gender=gender

        #getter
    def getcustomerid(self):
        return self.customerid
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
    def getgender(self):
        return self.gender

    #setter
    def setcustomerid(self,customerid):
        self.customerid=customerid
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
    def setgender(self,gender):
        self.gender=gender

    #str/tostring
    def __str__(self):
        return("{}, {}, {}, {}, {}, {}, {}".format(self.customerid,self.name,self.phone,self.address,self.username,self.password,self.gender))

