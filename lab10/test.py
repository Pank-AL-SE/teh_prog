import unittest
from unittest.mock import patch

from main import TMember, TPoly

class TestTMember(unittest.TestCase):
    def setUp(self):
        self.member_1 = TMember(6, 3)
        self.member_2 = TMember(3, 0)
        self.member_3 = TMember(-2, 2)
        self.member_4 = TMember(0, 0)
        self.member_5 = TMember(2, 1)

    def test_constructor(self):
        self.assertEqual(self.member_1.get_coeff(), 6)
        self.assertEqual(self.member_1.get_degree(), 3)
        self.assertEqual(self.member_2.get_coeff(), 3)
        self.assertEqual(self.member_2.get_degree(), 0)
        self.assertEqual(self.member_3.get_coeff(), -2)
        self.assertEqual(self.member_3.get_degree(), 2)
        self.assertEqual(self.member_4.get_coeff(), 0)
        self.assertEqual(self.member_4.get_degree(), 0)
        self.assertEqual(self.member_5.get_coeff(), 2)
        self.assertEqual(self.member_5.get_degree(), 1)

    def test_get_set_coeff(self):
        self.member_1.set_coeff(10)
        self.assertEqual(self.member_1.get_coeff(), 10)
        self.member_1.set_coeff(20)
        self.assertEqual(self.member_1.get_coeff(), 20)

    def test_get_set_degree(self):
        self.member_1.set_degree(4)
        self.assertEqual(self.member_1.get_degree(), 4)
        self.member_1.set_degree(5)
        self.assertEqual(self.member_1.get_degree(), 5)

    def test_is_equal(self):
        self.assertTrue(self.member_2.is_equal(TMember(3, 0)))
        self.assertFalse(self.member_1.is_equal(self.member_2))

    def test_differentiate(self):
        self.assertEqual(self.member_1.differentiate().get_coeff(), 18)
        self.assertEqual(self.member_1.differentiate().get_degree(), 2)
        self.assertEqual(self.member_2.differentiate().get_coeff(), 0)
        self.assertEqual(self.member_2.differentiate().get_degree(), 0)

    def test_evaluate(self):
        self.assertAlmostEqual(self.member_1.evaluate(2), 48)
        self.assertAlmostEqual(self.member_2.evaluate(5), 3)
        self.assertAlmostEqual(self.member_3.evaluate(-1), -2)

    def test_to_string(self):
        self.assertEqual(self.member_1.to_string(), "6x^3")
        self.assertEqual(self.member_2.to_string(), "3")
        self.assertEqual(self.member_3.to_string(), "-2x^2")
        self.assertEqual(self.member_4.to_string(), "0")
        self.assertEqual(self.member_5.to_string(), "2x")

class TestTPoly(unittest.TestCase):
    def setUp(self):
        self.poly_1 = TPoly([TMember(6, 3)])
        self.poly_2 = TPoly([TMember(3, 0)])
        self.poly_3 = TPoly([TMember(-2, 2)])
        self.poly_4 = TPoly([])
        self.poly_5 = TPoly([TMember(2, 1)])

    def test_constructor(self):
        self.assertEqual(self.poly_1.members, [TMember(6, 3)])
        self.assertEqual(self.poly_2.members, [TMember(3, 0)])
        self.assertEqual(self.poly_3.members, [TMember(-2, 2)])
        self.assertEqual(self.poly_4.members, [])

    def test_degree(self):
        self.assertEqual(self.poly_1.degree, 3)
        self.assertEqual(self.poly_2.degree, 0)
        self.assertEqual(self.poly_3.degree, 2)
        self.assertEqual(self.poly_4.degree, -1)

    def test_coefficient(self):
        self.assertEqual(self.poly_1.coefficient(3), 6)
        self.assertEqual(self.poly_2.coefficient(0), 3)
        self.assertEqual(self.poly_3.coefficient(2), -2)
        self.assertEqual(self.poly_4.coefficient(0), 0)

    def test_clear(self):
        self.poly_1.clear()
        self.assertEqual(self.poly_1.members, [])

    def test_add(self):
        sum_poly_12 = self.poly_1.add(self.poly_2)
        self.assertEqual(sum_poly_12.members, [TMember(6, 3), TMember(3, 0)])
        sum_poly_34 = self.poly_3.add(self.poly_4)
        self.assertEqual(sum_poly_34.members, [TMember(-2, 2)])

    def test_multiply(self):
        prod_poly_13 = self.poly_1.multiply(self.poly_3)
        self.assertEqual(prod_poly_13.members, [TMember(-12, 5)])
        prod_poly_24 = self.poly_2.multiply(self.poly_4)
        self.assertEqual(prod_poly_24.members, [])

    def test_subtract(self):
        diff_poly_23 = self.poly_2.subtract(self.poly_3)
        self.assertEqual(diff_poly_23.members, [TMember(2, 2), TMember(3, 0)])
        diff_poly_14 = self.poly_1.subtract(self.poly_4)
        self.assertEqual(diff_poly_14.members, [TMember(6, 3)])

    def test_negate(self):
        neg_poly_1 = self.poly_1.negate()
        self.assertEqual(neg_poly_1.members, [TMember(-6, 3)])

    def test_equals(self):
        poly_copy_1 = TPoly([TMember(6, 3)])
        self.assertTrue(self.poly_1.equals(poly_copy_1))
        self.assertFalse(self.poly_1.equals(self.poly_2))

    def test_differentiate(self):
        diff_poly_1 = self.poly_1.differentiate()
        self.assertEqual(diff_poly_1.members, [TMember(18, 2)])
        diff_poly_2 = self.poly_2.differentiate()
        self.assertEqual(diff_poly_2.members, [])

    def test_evaluate(self):
        self.assertAlmostEqual(self.poly_1.evaluate(2), 48)
        self.assertAlmostEqual(self.poly_2.evaluate(5), 3)
        self.assertAlmostEqual(self.poly_3.evaluate(-1), -2)

if __name__ == '__main__':
    unittest.main()