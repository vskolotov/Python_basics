from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size=0):
        self.size = size

    @property
    def fabric_consumption(self):
        if self.size == 0:
            return f'{0:.2f} m.'
        else:
            return f'{self.size / 6.5 + 0.5:.2f} m.'


class Suit(Clothes):
    def __init__(self, height=0):
        self.height = height

    @property
    def fabric_consumption(self):
        if self.height != 0:
            return f'{2 * self.height + 0.3:.2f} m.'
        else:
            return f'{0:.2f} m.'


p = Coat(48)
print(p.fabric_consumption)
k = Suit(170)
print(k.fabric_consumption)
