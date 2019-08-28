class Pizza:

    def __init__(self):
        self.type = "",
        self.size = "",
        self.toppings1 = ""
        self.toppings2 = ""
        self.toppings = []

    def add_toppings(self, topping):
        self.toppings.append(topping)

    def print_order(self):
        print(f"Your pizza is a {self.type}, {self.size}, with {', '.join(self.toppings)}")


meat_pizza = Pizza() 
meat_pizza.type = "flatbread"
meat_pizza.size = "16 inch"
meat_pizza.add_toppings("sausage")
meat_pizza.add_toppings("bacon")
meat_pizza.print_order()

veg_pizza = Pizza()
veg_pizza.type = "deep-dish"
veg_pizza.size = "8 inch"
veg_pizza.add_toppings("peppers")
veg_pizza.add_toppings("onions")
veg_pizza.print_order()


