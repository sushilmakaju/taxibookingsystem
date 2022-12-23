class adminlibs():
    def __init__(self,admin_id=0, username=None, password=None, phoneNo=None, email=None):
        self.admin_id=admin_id
        self.username=username
        self.password=password
        self.phoneNo=phoneNo
        self.email=email

    def getadminid(self):
        return self.admin_id
    def getusername(self):
        return self.username
    def getpassword(self):
        return self.password
    def getphoneNo(self):
        return self.phoneNo
    def getemail(self):
        return self.email

    def setadmin_id(self,admin_id):
        self.admin_id=admin_id
    def setusername(self,username):
        self.username=username
    def setpassword(self,password):
        self.password=password
    def setphoneNo(self,phoneNo):
        self.phoneNo=phoneNo
    def setemail(self,email):
        self.email=email

    #str/tostring

    def __str__(self):
        return ("{}, {}, {}, {}, {}".format(self.admin_id, self.username, self.password, self.phoneNo, self.email))
