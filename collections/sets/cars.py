showroom = set()

showroom = {"Honda", "Jeep", "Mustang", "Subaru"}

print(len(showroom))

showroom.add("Jeep")

print(showroom)

more_cars = set()

more_cars = {"Ford", "Toyota"}

showroom.update(more_cars)

showroom.discard("Jeep")

junkyard = {"Crosstrek", "Toyota", "Mustang", "Jaguar"}

print("Same Cars", showroom.intersection(junkyard))

junkyard.discard("Crosstrek")