import random

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(0, 6, 1))

# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for number in range(0, 6):
    if my_randoms.__contains__(number):
        print(f"my_randoms contain {number}")
    else: 
        print(f"my_randoms does not contain {number}")
        

