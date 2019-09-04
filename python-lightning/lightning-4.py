# Define a class called Boat
# Give it a method that allows the boat to move that prints the speed it's moving
# Define a Class called Kayak
# Make it a derived class of Boat
# Give it a method called paddle that uses its inherited move method
# Make a Kayak instance and 'paddle' it

class Boat():

    def _init__(self, speed):
        self.speed = speed

    def move_boat(self):
        print(f"The boat is moving at {self.speed}mph.")


class Kayak(Boat):

    def __init__(self, passangers=1):
        super().__init__("5")
        self.passangers = passangers

    def paddle(self):
        self.move_boat()

my_kayak = Kayak()

my_kayak.paddle()
