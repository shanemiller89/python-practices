from building import Building, building_1, building_2
from city import City


Mega_City = City("MEGA CITY", "Joe Shep", "2012")

Mega_City.add_building(building_1)
Mega_City.add_building(building_2)

for building in Mega_City.buildings:
    print(building) 

       