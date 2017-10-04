class Bike(object):
    def __init__(self, price, max_speeds, miles,name):
        self.price = price
        self.max_speeds= max_speeds
        self.miles = miles
        self.name = name
    def displayInfo(self):
        print "****Inside method display ***"
        print "You are on ", self.name
        print "Price:", self.price
        print "Speed:", self.max_speeds
        print "Miles:", self.miles
        return self
        # print self.max_speeds
        # print self.miles
    def ride(self):
        print "***Inside method Riding***"
        print "Riding"
        self.miles += 10
        print "Miles after current ride:", self.miles
        return self
    def reverse(self):
        print "***Inside method reverse***"
        print "Reversing"
        if(self.miles == 0):
            print "Your at zero miles"
            print "Cant reverse else your miles will be negative"
        else :
            self.miles -= 5
            print "miles after reverse:",self.miles    
        return self
# object creation       
bike1 = Bike(100000,80, 200,"bike1")
# calling all functions for bike1
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

# object creation       
bike2 = Bike(12000,90, 200, "bike2")
# calling all functions for bike1
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

# object creation       
bike3 = Bike(20000,30, 200, "bike3")
# calling all functions for bike1
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()

# method chaining
print "###Method chainig for bike1!!!######"
bike1.ride().ride().ride().reverse().displayInfo()




