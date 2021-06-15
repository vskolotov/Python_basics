class Matrix:
    def __init__(self, lists):
        self.matrix = lists

    def __str__(self):
        self.s = ''
        for i in self.matrix:
            self.s += f'{i}\n'
        return self.s

    def __add__(self, other):
        self.summa = ([[] for i in range(len(self.matrix))])
        for i in range(len(self.matrix)):
            self.el = []
            for j in range(len(self.matrix[i])):
                self.el.append(self.matrix[i][j] + other.matrix[i][j])
            self.summa[i] = self.el
        return Matrix(self.summa)


a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
b = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b)
print(a + b)


