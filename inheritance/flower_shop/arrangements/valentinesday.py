from .arrangement import Arrangement

class ValentinesDay(Arrangement):

    def __init__(self):
        super().__init__()

    def enhance(self, flower):
        self.flowers.append(flower)