class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        if self.b + other.b >= 0:
            return f'{self.a + other.a}+{self.b + other.b}i'
        else:
            return f'{self.a + other.a}{self.b + other.b}i'

    def __mul__(self, other):
        self.A = self.a * other.a - self.b * other.b
        self.B = self.b * other.a + self.a * other.b
        if self.B >= 0:
            return f'{self.A}+{self.B}i'
        else:
            return f'{self.A}{self.B}i'

    def __str__(self):
        if self.b >= 0:
            return f'{self.a}+{self.b}i'
        else:
            return f'{self.a}{self.b}i'


a = ComplexNumber(1, -1)
print(a)
b = ComplexNumber(3, -6)
print(b)
print(a + b)
print(a * b)
