class Vehicle():

    def __init__(self, manufacturer, model, fuel_capacity,horsepower, wheel_count):
        self.manufacturer = manufacturer
        self.model = model
        self.fuel_capacity = fuel_capacity
        self.gas_level = 0
        self.horsepower = horsepower
        self.wheel_count = wheel_count

    def drive(self, lowerby):
        self.gas_level = self.gas_level - lowerby
        print(f"You have {self.gas_level} gallons left.")
    
    def refuel(self):
        self.gas_level = self.fuel_capacity