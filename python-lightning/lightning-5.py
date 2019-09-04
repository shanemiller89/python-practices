

def add(x, y):
    sum = x + y
    return sum

def subtract(x, y):
    difference = x - y
    return difference


def calculate(function):
    return function(3, 5)

print(calculate(add(3,4)))
print(calculate(subtract(3, 4)))