from vehicle import Vehicle
# 1. Create a Dodge Ram class
#     * `manufacturer` attribute
#     * `model` attribute
#     * `fuel_capacity` attribute
#     * `gas_level` attribute
#     * `horsepower` attribute
#     * `wheel_count` attribute
#     * `drive()` method lowers `gas_level` by 4 each time it is invoked
#     * `refuel()` method method sets `gas_level` to `fuel_capacity` value

class Ram(Vehicle):

    def __init__(self):
        super().__init__("Dodge", "Ram", 26, 395, 4)
   
    def drive(self):
        super().drive(6)


    # def drive(self):
    #     self.gas_level = self.gas_level - 4
    # print(f"You have {self.gas_level} gallons left in your Dodge Ram")
    