# class which has a class parameter and a instance parameter

class Car:
    name = "Car"

    def __init__(self,name = None):
        self.name = name

Merc = Car('Mercedes')        
print("%s name is %s"%(Car.name,Merc.name))


toyota = Car()
toyota.name ="Toyota"
print("%s name is %s"%(Car.name,toyota.name))

