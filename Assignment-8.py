class vehicle:
    def move(self):
        print("The vehivle is moving.")
class car(vehicle):
    def move(self):
        print("Driving on the road.")
class bicycle(vehicle):
    def move(self):
        print("Pedaling on the road") 

vehicles=[car(),bicycle()] 
for vehicle in vehicles:
    vehicle.move()             