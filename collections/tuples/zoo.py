zoo = ("Zebra", "Giraffe", "Lion", "Bear", "Monkey" )

print(zoo.index("Zebra"))

animal_to_find = "Kangaroo"

if animal_to_find in zoo:
    print(f"{animal_to_find} is in the zoo")
else: 
    print(f"{animal_to_find} is not in the zoo")

(first_animal, second_animal, third_animal, fourth_animal, fifth_animal) = zoo

print(first_animal)
print(second_animal)
print(third_animal)

new_zoo = list(zoo)

new_zoo.extend(["Tigers", "Kangaroo", "Jaguar"])

new_zoo_tuple = tuple(new_zoo)

print(new_zoo_tuple)

# print(first_animal)