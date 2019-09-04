# 1. Create a Nissan Leaf class
#     * `manufacturer` attribute
#     * `model` attribute
#     * `battery_capacity` attribute
#     * `battery_level` attribute
#     * `horsepower` attribute
#     * `wheel_count` attribute
#     * `drive()` method lowers `battery_level` by 2 each time it is invoked
#     * `recharge()` method sets `battery_level` to `battery_capacity` value

class Leaf(Vehicle):

    def __init__(self):
        super().__init__("Nissan", "Leaf", 0, 320, 4)
        self.battery_capacity = 400
        self.battery_level = 0
 
    def drive(self):
        self.battery_level -= 2
        print(f"Your battery is at {self.battery_level} out of {self.battery_capacity}")

    def recharge(self):
        self.battery_level = self.battery_capacity