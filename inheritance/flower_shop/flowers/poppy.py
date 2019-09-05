from .flower import Flower
from .organic import Organic

class Poppy(Flower, Organic):
    def __init__(self, color, stem_length):
        Flower.__init__(self, color, stem_length)
        Organic.__init__(self)