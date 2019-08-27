def print_numbers():
    numbers = range(1,100)
    for number in numbers:
        if number%5 == 0 & number%7 == 0:
            print("ChickenMonkey")
        if number%5 == 0: 
            print("Chicken")
        if number%7 == 0:
            print("Monkey")


print_numbers()