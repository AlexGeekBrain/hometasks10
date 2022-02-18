from abc import ABC, abstractmethod


class Clothes(ABC):
    result = 0

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consume(self):
        pass

    def __add__(self, other):
        Clothes.result += self.consume + other.consume
        return Costume(0)

    def __str__(self):
        res = Clothes.result
        Clothes.result = 0
        return f'{res}'


class Coat(Clothes):
    @property
    def consume(self):
        return round(self.param / 6.5) + 0.5


class Costume(Clothes):
    @property
    def consume(self):
        return round(2 * self.param + 0.3) / 100


coat = Coat(50)
costume = Costume(150)
print(coat + costume)
