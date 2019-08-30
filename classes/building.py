import datetime

class Building: 

    def __init__(self, address, stories):
        self.designer = "Shane Miller",
        self.date_constructed = "",
        self.owner = "",
        self.address = address,
        self.stories = stories

    def construct(self):
        self.date_constructed = datetime.datetime.now()
    
    def purchase(self, owner):
        self.owner = owner
    
    def show_building(self):
        print(f"The building, at {self.address} and designed by {self.designer}, has {self.stories} is owned by {self.owner} and was built on {self.date_constructed}.")

    def __str__(self):
        return f'Designer: {self.designer}, Date Made: {self.date_constructed}, Owner: {self.owner} Address: {self.address}, Stories: {self.stories}'

building_1 = Building('123 Main St.', 5)
building_1.purchase("Ben")
building_1.construct()
# building_1.show_building()

building_2 = Building('456 Main St.', 14)
building_2.purchase("Amber")
building_2.construct()
# building_2.show_building()







