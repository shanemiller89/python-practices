# Define 5 of your favorite vehicles
# Move all common properties in your vehicles to a new Vehicle class.
# Create an instance of each vehicle.
# Define a different value for each vehicle's properties.
# Create a drive() method in the Vehicle class.
# Override the drive() method in all the other vehicle classes. Include the vehicle's color in the message (i.e. "The blue Ram drives past. RRrrrrrummbbble!").
# Create a turn(self, direction) method, and a stop(self) method on Vehicle. Define a basic implementation of each.
# Override all three of those methods on some of the vehicles. For example, the stop() method for a plane would be to output the message "The white Cessna rolls to a stop after rolling a mile down the runway."
# Make your vehicle instances perform all three behaviors.


class Vehicle:

    def __init__(self):
        self.color = ""
        self.occupancy = ""

    def drive(self):
        print("Vrrrrooooom")

class Subaru(Vehicle):
    
    def __init__(self, fuel):
        self.fuel = ""

    def drive(self):
        print(f"The {self.color} Subaru goes VaVaVahrroom")

class Tesela(Vehicle):

    def __init__(self):
        self.battery = ""
   
    def drive(self):
        print(f"The {self.color} Tesela goes Beep Boop Beep Boop")

crosstrek = Subaru("23mpg")
modells = Tesela()

crosstrek.color = "Pearl"
crosstrek.occupancy = 5

modells.color = "Blue"
modells.occupancy = 5

crosstrek.drive()
modells.drive