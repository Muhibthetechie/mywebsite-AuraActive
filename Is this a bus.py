class Vechile:
    def __init__(self,name,max_speed,milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage
class bus(Vechile):
    pass
School_bus = bus("School Volvo" , 180 , 12)
print("School bus name is" , School_bus.name , "The max speed is", School_bus.max_speed,"The milage is", School_bus.milage)