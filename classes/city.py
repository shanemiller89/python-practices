class City():

    def __init__(self, city_name, mayor, year_created):
        self.city_name = city_name
        self.mayor = mayor
        self.year_created = year_created
        self.buildings = []

    def add_building(self, building):
        self.buildings.append(building)

