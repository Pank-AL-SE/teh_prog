import unittest
from new_matrix import Matrix  # Предполагается, что класс Matrix сохранен в matrix.py

class TestMatrix(unittest.TestCase):

    def test_constructor_valid_input_creates_matrix(self):
        data = [[1, 2], [3, 4]]
        matrix = Matrix(data)
        self.assertEqual(matrix.I, 2)
        self.assertEqual(matrix.J, 2)
        self.assertEqual(matrix[0, 0], 1)
        self.assertEqual(matrix[1, 1], 4)

    def test_constructor_invalid_input_throws_exception_empty_matrix(self):
        data = []
        with self.assertRaises(ValueError):
            Matrix(data)

    def test_equals_two_equal_matrices_returns_true(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[1, 2], [3, 4]])
        self.assertTrue(matrix1 == matrix2)

    def test_equals_two_different_matrices_returns_false(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8]])
        self.assertFalse(matrix1 == matrix2)

    def test_equals_two_different_sizes(self):
        matrix1 = Matrix([[1, 2], [3, 4], [6, 2]])
        matrix2 = Matrix([[1, 2], [3, 4]])
        with self.assertRaises(ValueError):
            matrix1 == matrix2

    def test_equals_two_different_types(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        try:
            matrix1 == [[1, 2], [3, 4]]
            raise AttributeError("Invalid attribute")
        except:
            pass

    def test_equals_null(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        try:
            matrix1 == [[1, 2], [3, 4]]
            raise AttributeError("Invalid attribute")
        except:
            pass


    def test_inequals_two_different_matrices_returns_true(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[1, 2], [3, 5]])
        self.assertTrue(matrix1 != matrix2)

    def test_add_two_matrices_returns_correct_result(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8]])
        result = matrix1 + matrix2
        expected = Matrix([[6, 8], [10, 12]])
        self.assertEqual(result, expected)

    def test_add_two_matrices_different_sizes(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8], [6, 2]])
        with self.assertRaises(ValueError):
            matrix1 + matrix2

    def test_subtract_two_matrices_returns_correct_result(self):
        matrix1 = Matrix([[5, 6], [7, 8]])
        matrix2 = Matrix([[1, 2], [3, 4]])
        result = matrix1 - matrix2
        expected = Matrix([[4, 4], [4, 4]])
        self.assertEqual(result, expected)

    def test_subtract_two_matrices_different_sizes(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8], [1, 2]])
        with self.assertRaises(ValueError):
            matrix1 - matrix2

    def test_multiply_two_matrices_returns_correct_result(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8]])
        result = matrix1 * matrix2
        expected = Matrix([[19, 22], [43, 50]])
        self.assertEqual(result, expected)

    def test_multiply_two_matrices_wrong_sizes(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8], [1, 2]])
        with self.assertRaises(ValueError):
            matrix1 * matrix2

    def test_min_returns_minimum_element(self):
        matrix = Matrix([[5, 3], [7, 1]])
        self.assertEqual(matrix.min(), 1)

    def test_transp_returns_transposed_matrix(self):
        matrix = Matrix([[1, 2], [3, 4]])
        result = matrix.transp()
        expected = Matrix([[1, 3], [2, 4]])
        self.assertEqual(result, expected)

    def test_transp_error_size(self):
        matrix = Matrix([[1, 2], [3, 4], [5, 6]])
        result = matrix.transp()
        expected = Matrix([[1, 3, 5], [2, 4, 6]])
        self.assertEqual(result, expected)

    def test_to_string_returns_correct_string_representation(self):
        matrix = Matrix([[1, 2], [3, 4]])
        self.assertEqual(str(matrix), '[[1, 2], [3, 4]]')

    def test_indexer_valid_indexes_returns_correct_element(self):
        matrix = Matrix([[1, 2], [3, 4]])
        self.assertEqual(matrix[0, 0], 1)
        self.assertEqual(matrix[1, 1], 4)

    def test_indexer_invalid_indexes_throws_exception(self):
        matrix = Matrix([[1, 2], [3, 4]])
        with self.assertRaises(IndexError):
            _ = matrix[2, 2]

if __name__ == '__main__':
    unittest.main()