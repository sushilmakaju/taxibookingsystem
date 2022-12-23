class bookinglibs():
    def __init__(self,booking_id=0, pickup_address=None, drop_address=None, pickup_time=None, pickup_date=None,booking_status=None, customer_id=0, driver_id=None):
        self.booking_id=booking_id
        self.pickup_address=pickup_address
        self.drop_address=drop_address
        self.pickup_time=pickup_time
        self.pickup_date=pickup_date
        self.booking_status=booking_status
        self.customer_id=customer_id
        self.driver_id=driver_id

    def getbooking_id(self):
        return self.booking_id
    def getpickup_address(self):
        return self.pickup_address
    def getdrop_address(self):
        return self.drop_address
    def getpickup_time(self):
        return self.pickup_time
    def getpickup_date(self):
        return self.pickup_date
    def getbooking_status(self):
        return self.booking_status
    def getcustomer_id(self):
        return self.customer_id
    def getdriver_id(self):
        return self.driver_id

    def setbooking_id(self,booking_id):
        self.booking_id=booking_id
    def setpickup_address(self,pickup_address):
        self.pickup_address=pickup_address
    def setdrop_address(self,drop_address):
        self.drop_address=drop_address
    def setpickup_time(self,pickup_time):
        self.pickup_time=pickup_time
    def setpickup_date(self,pickup_date):
        self.pickup_date=pickup_date
    def setbooking_status(self,booking_status):
        self.booking_status=booking_status
    def setcustomer_id(self,customer_id):
        self.customer_id=customer_id
    def setdriver_id(self,driver_id):
        self.driver_id=driver_id

    #str/tostring
    def __str__(self):
        return("{}, {}, {}, {}, {}, {}, {}, {}".format(self.booking_id,self.pickup_address,self.drop_address,self.pickup_time,self.pickup_date,self.booking_status,self.customer_id,self.driver_id))