import numpy as np

class Matrix:
    def __init__(self, matrix):
        if len(matrix) < 1 or len(matrix[0]) < 1:
            raise ValueError("The number of rows and columns must be greater than 0")
        self.matrix = np.array(matrix, dtype=int)
        self.I = self.matrix.shape[0]
        self.J = self.matrix.shape[1]

    def __getitem__(self, indices):
        i, j = indices
        if i < 0 or i >= self.I or j < 0 or j >= self.J:
            raise IndexError("Indexes are out of range of acceptable values")
        return self.matrix[i, j]

    def __add__(self, other):
        if self.I != other.I or self.J != other.J:
            raise ValueError("Matrices must be of the same sizes")
        result = self.matrix + other.matrix
        return Matrix(result)

    def __sub__(self, other):
        if self.I != other.I or self.J != other.J:
            raise ValueError("Matrices must be of the same sizes")
        result = self.matrix - other.matrix
        return Matrix(result)

    def __mul__(self, other):
        if self.J != other.I:
            raise ValueError("Matrices are not consistent for multiplication")
        result = np.dot(self.matrix, other.matrix)
        return Matrix(result)

    def __eq__(self, other):
        if self.I != other.I or self.J != other.J:
            raise ValueError("Matrices must be of the same sizes")
        return np.array_equal(self.matrix, other.matrix)

    def __ne__(self, other):
        return not self == other

    def transp(self):
        result = self.matrix.T
        return Matrix(result)

    def min(self):
        return np.min(self.matrix)

    def __str__(self):
        return str(self.matrix.tolist())

    def __repr__(self):
        return f"Matrix({self.matrix.tolist()})"

# Пример использования:
# a = Matrix([[1, 2], [3, 4]])
# b = Matrix([[5, 6], [7, 8]])
# print(a + b)
# print(a * b)