class Cell:
    def __init__(self, integer=0):
        self.integer = integer

    def __add__(self, other):
        return Cell(self.integer + other.integer)

    def __sub__(self, other):
        return Cell(self.integer - other.integer)

    def __mul__(self, other):
        return Cell(self.integer * other.integer)

    def __floordiv__(self, other):
        return Cell(self.integer // other.integer)

    def __truediv__(self, other):
        return Cell(self.integer // other.integer)

    def __str__(self):
        if self.integer >= 0:
            return f'{self.integer}'
        else:
            return f'operation is not possible'

    def make_order(self, cells_in_row):
        self.s = ''
        self.cells_in_row = cells_in_row
        for i in range(1, self.integer + 1):
            if i % self.cells_in_row == 0:
                if i == self.integer:
                    self.s += '*'
                else:
                    self.s += '*\\n'
            else:
                self.s += '*'
        return self.s


a = Cell(15)
b = Cell(45)
print(a + b)
print(a - b)
print(b - a)
print(b * a)
print(b / a)
print(b // a)
print(a.make_order(5))
print(a.cells_in_row)
