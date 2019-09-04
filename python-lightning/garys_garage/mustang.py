from vehicle import Vehicle

# 1. Create a Ford Mustang class
#     * `manufacturer` attribute
#     * `model` attribute
#     * `fuel_capacity` attribute
#     * `gas_level` attribute
#     * `horsepower` attribute
#     * `wheel_count` attribute
#     * `drive()` method lowers `gas_level` by 4 each time it is invoked
#     * `refuel()` method method sets `gas_level` to `fuel_capacity` value

class Mustang(Vehicle):

    def __init__(self):
        super().__init__("Ford", "Mustang", 20, 460, 4)

    def drive(self):
        super().drive(4)
    
    # def refuel(self):
    #     self.gas_level = self.fuel_capacity
