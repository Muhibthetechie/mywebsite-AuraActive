class Vehicle:
    def __init__(self,max_speed,milage):

        self.max_speed = max_speed
        self.milage = milage

modelX = Vehicle(240,18)

print("The max speed is ", modelX.max_speed)
print("The milage is" , modelX.milage)
