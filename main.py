"""Задача 1"""


class Matrix:
    def __init__(self, matrix=list):
        self.matrix = matrix

    def __str__(self):
        """
        Каждый внутренний список - это строка
        :return: возвращает str из списков, являющихся строками матрицы
        """
        result = ''
        for string in self.matrix:
            result = result + str(string) + '\n'
        return result

    def __add__(self, other):
        """
        Любая матрица имеет размерность m*n, где m - количество элементов строки, n - количество строк.
        Обязательное условия сложения матриц - одинаковая размерность
        :param other: вторая матрица
        :return: результат сложения, матрица
        """
        result = []
        for string_1 in self.matrix:
            result.append(string_1)
        for i in range(len(other.matrix)):
            for j in range(len(other.matrix[i])):
                result[i][j] += other.matrix[i][j]
        return Matrix(result)

m = [[2, 4, 6], [1, 3, 5], [7, 8, 9]]
n = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
matrix_1 = Matrix(m)
matrix_2 = Matrix(n)
print(matrix_1)
print(matrix_2)
matrix_3 = matrix_1 + matrix_2
print(matrix_3)


"""Задача 2"""


from abc import ABC, abstractmethod


class Clothe(ABC):

    @abstractmethod
    def textile(self):
        pass


class Coat(Clothe):
    def __init__(self, v):
        self.v = v

    @property
    def textile(self):
        return self.v/6.5 + 0.5


class Costume(Clothe):
    def __init__(self, h):
        self.h = h

    @property
    def textile(self):
        return 2*self.h + 0.3


coat = Coat(10)
costume = Costume(10)
print(coat.textile)
print(costume.textile)


"""Задача 3"""


class Cell:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return Cell(self.n + other.n)

    def __sub__(self, other):
        if self.n - other.n > 0:
            return Cell(self.n - other.n)
        else: print('Разность ячеек не превосходит 0')

    def __mul__(self, other):
        return Cell(self.n * other.n)

    def __truediv__(self, other):
        return Cell(self.n // other.n)

    def make_order(self, row=int):
        if self.n < row:
            return '*' * (self.n % row)
        else:
            return ('*' * row + '\n') * (self.n // row) + '*' * (self.n % row)


cell_1 = Cell(15)
cell_2 = Cell(12)
cell_3 = cell_1 + cell_2
print(cell_3.make_order(5))