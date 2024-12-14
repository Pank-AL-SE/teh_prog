import unittest
from TPNumbeer import TPNumber

class TPNumberTest(unittest.TestCase):
    def test_constructor_double_base_precision(self):
        num1 = TPNumber(10.0, 10, 2)
        self.assertAlmostEqual(num1.number(), 10.0)
        self.assertEqual(num1.base(), 10)
        self.assertEqual(num1.precision(), 2)

        num2 = TPNumber(234.153, 5, 8)
        self.assertEqual(num2.numberString(), "1414.03403030")
        self.assertEqual(num2.base(), 5)
        self.assertEqual(num2.precision(), 8)

    def test_constructor_double_base_precision_exceptions(self):
        with self.assertRaises(ValueError):
            TPNumber(10.0, 20, 2)
        with self.assertRaises(ValueError):
            TPNumber(10.0, 1, 2)
        with self.assertRaises(ValueError):
            TPNumber(10.0, 6, -1)

    def test_constructor_string_base_precision_exceptions(self):
        with self.assertRaises(ValueError):
            TPNumber("10.0", "20", "2")
        with self.assertRaises(ValueError):
            TPNumber("10.0", "1", "2")
        with self.assertRaises(ValueError):
            TPNumber("10.0", "6", "-1")
        with self.assertRaises(ValueError):
            TPNumber("1~0.0", "6", "1")
        with self.assertRaises(ValueError):
            TPNumber("80.0", "6", "1")
        with self.assertRaises(ValueError):
            TPNumber("10.0", "Z", "2")
        with self.assertRaises(ValueError):
            TPNumber("10.0", "q`sdfa", "1")
        with self.assertRaises(ValueError):
            TPNumber("1~0.0", "6", "1")
        with self.assertRaises(ValueError):
            TPNumber("80.0", "6", "1")
        with self.assertRaises(ValueError):
            TPNumber("10.0", "Z", "2")
        with self.assertRaises(ValueError):
            TPNumber("10.0", "`dsgfa", "1")

    def test_constructor_string_base_precision(self):
        num2 = TPNumber("-A.B9", "16", "4")
        self.assertAlmostEqual(num2.number(), -10.7227, 4)
        self.assertEqual(num2.base(), 16)
        self.assertEqual(num2.precision(), 4)

    def test_set_base_from_int(self):
        num1 = TPNumber(10.0, 10, 2)
        num1.setBase(2)
        self.assertEqual(num1.base(), 2)

    def test_set_base_from_int_exceptions(self):
        num1 = TPNumber("10.0", "3", "2")
        with self.assertRaises(ValueError):
            num1.setBase(20)
        with self.assertRaises(ValueError):
            num1.setBase(1)

    def test_set_base_from_string(self):
        num1 = TPNumber(10.0, 10, 2)
        num1.setBase("8")
        self.assertEqual(num1.base(), 8)

    def test_set_base_from_string_exceptions(self):
        num1 = TPNumber("10.0", "3", "2")
        with self.assertRaises(ValueError):
            num1.setBase("20")
        with self.assertRaises(ValueError):
            num1.setBase("1")
        with self.assertRaises(ValueError):
            num1.setBase("q`sdfa")
        with self.assertRaises(ValueError):
            num1.setBase("`dsgfa")
        with self.assertRaises(ValueError):
            num1.setBase("Z")
        with self.assertRaises(ValueError):
            num1.setBase("q`sdfa")
        with self.assertRaises(ValueError):
            num1.setBase("Z")

    def test_set_precision_from_int(self):
        num1 = TPNumber(10.0, 10, 2)
        num1.set_precision(4)
        self.assertEqual(num1.precision(), 4)

    def test_set_precision_from_int_exceptions(self):
        num1 = TPNumber("10.0", "3", "2")
        with self.assertRaises(ValueError):
            num1.set_precision(-1)

    def test_set_precision_from_string(self):
        num1 = TPNumber(10.0, 10, 2)
        num1.set_precision("5")
        self.assertEqual(num1.precision(), 5)

    def test_set_precision_from_string_exceptions(self):
        num1 = TPNumber("10.0", "3", "2")
        with self.assertRaises(ValueError):
            num1.set_precision("-1")
        with self.assertRaises(ValueError):
            num1.set_precision("`dsgfa")
        with self.assertRaises(ValueError):
            num1.set_precision("`dsgfa")
        with self.assertRaises(ValueError):
            num1.set_precision("Z")
        with self.assertRaises(ValueError):
            num1.set_precision("q`sdfa")
        with self.assertRaises(ValueError):
            num1.set_precision("Z")

    def test_addition(self):
        num1 = TPNumber(10.0, 10, 2)
        num4 = TPNumber(20.0, 10, 2)
        result = num1 + num4
        self.assertAlmostEqual(result.number(), 30.0)
        self.assertEqual(result.base(), 10)
        self.assertEqual(result.precision(), 2)

    def test_operations_exceptions_base(self):
        num1 = TPNumber(10.0, 10, 2)
        num4 = TPNumber(20.0, 12, 2)
        with self.assertRaises(ValueError):
            result = num1 + num4
        with self.assertRaises(ValueError):
            result = num1 - num4
        with self.assertRaises(ValueError):
            result = num1 * num4
        with self.assertRaises(ValueError):
            result = num1 / num4

    def test_operations_exceptions_precision(self):
        num1 = TPNumber(10.0, 10, 4)
        num4 = TPNumber(20.0, 10, 2)
        with self.assertRaises(ValueError):
            result = num1 + num4
        with self.assertRaises(ValueError):
            result = num1 - num4
        with self.assertRaises(ValueError):
            result = num1 * num4
        with self.assertRaises(ValueError):
            result = num1 / num4

    def test_operations_exceptions_division_by_zero(self):
        num1 = TPNumber(10.0, 10, 4)
        num4 = TPNumber(0.0, 10, 4)
        with self.assertRaises(ValueError):
            result = num1 / num4

    def test_subtraction(self):
        num1 = TPNumber(10.0, 10, 2)
        num4 = TPNumber(20.0, 10, 2)
        result = num4 - num1
        self.assertAlmostEqual(result.number(), 10.0)
        self.assertEqual(result.base(), 10)
        self.assertEqual(result.precision(), 2)

    def test_multiplication(self):
        num1 = TPNumber(10.0, 10, 2)
        num4 = TPNumber(20.0, 10, 2)
        result = num1 * num4
        self.assertAlmostEqual(result.number(), 200.0)
        self.assertEqual(result.base(), 10)
        self.assertEqual(result.precision(), 2)

    def test_division(self):
        num1 = TPNumber(10.0, 10, 2)
        num4 = TPNumber(20.0, 10, 2)
        result = num4 / num1
        self.assertAlmostEqual(result.number(), 2.0)
        self.assertEqual(result.base(), 10)
        self.assertEqual(result.precision(), 2)

    def test_addition_ref(self):
        num1 = TPNumber(10.0, 10, 2)
        num4 = TPNumber(20.0, 10, 2)
        result = num1 + num4
        self.assertAlmostEqual(result.number(), 30.0)
        self.assertEqual(result.base(), 10)
        self.assertEqual(result.precision(), 2)

    def test_operations_exceptions_base_ref(self):
        num1 = TPNumber(10.0, 4, 2)
        num4 = TPNumber(20.0, 10, 2)
        with self.assertRaises(ValueError):
            result = num1 + num4
        with self.assertRaises(ValueError):
            result = num1 - num4
        with self.assertRaises(ValueError):
            result = num1 * num4
        with self.assertRaises(ValueError):
            result = num1 / num4

    def test_operations_exceptions_precision_ref(self):
        num1 = TPNumber(10.0, 10, 4)
        num4 = TPNumber(20.0, 10, 2)
        with self.assertRaises(ValueError):
            result = num1 + num4
        with self.assertRaises(ValueError):
            result = num1 - num4
        with self.assertRaises(ValueError):
            result = num1 * num4
        with self.assertRaises(ValueError):
            result = num1 / num4

    def test_division_by_zero_ref(self):
        num1 = TPNumber(10.0, 10, 4)
        num4 = TPNumber(0.0, 10, 4)
        with self.assertRaises(ValueError):
            result = num1 / num4

    def test_subtraction_ref(self):
        num1 = TPNumber(10.0, 10, 2)
        num4 = TPNumber(20.0, 10, 2)
        result = num1 - num4
        self.assertAlmostEqual(result.number(), -10.0)
        self.assertEqual(result.base(), 10)
        self.assertEqual(result.precision(), 2)

    def test_multiplication_ref(self):
        num1 = TPNumber(10.0, 10, 2)
        num4 = TPNumber(20.0, 10, 2)
        result = num1 * num4
        self.assertAlmostEqual(result.number(), 200.0)
        self.assertEqual(result.base(), 10)
        self.assertEqual(result.precision(), 2)

    def test_division_ref(self):
        num1 = TPNumber(10.0, 10, 2)
        num4 = TPNumber(20.0, 10, 2)
        result = num4 / num1
        self.assertAlmostEqual(result.number(), 2.0)
        self.assertEqual(result.base(), 10)
        self.assertEqual(result.precision(), 2)

    def test_invert(self):
        num1 = TPNumber(10.0, 10, 2)
        result = num1.Invert()
        self.assertAlmostEqual(result.number(), 0.1)
        self.assertEqual(result.base(), 10)
        self.assertEqual(result.precision(), 2)
        del num1
        del result

    def test_invert_exception(self):
        num1 = TPNumber(0.0, 10, 2)
        with self.assertRaises(ValueError):
            result = num1.Invert()

    def test_square(self):
        num1 = TPNumber(10.0, 10, 2)
        result = num1.Square()
        self.assertAlmostEqual(result.number(), 100.0)
        self.assertEqual(result.base(), 10)
        self.assertEqual(result.precision(), 2)
        del num1
        del result

    def test_division_by_zero(self):
        num1 = TPNumber(10.0, 10, 2)
        num4 = TPNumber(0.0, 10, 2)
        with self.assertRaises(ValueError):
            result = num1 / num4
        del num1
        del num4

    def test_division_by_zero_ref(self):
        num1 = TPNumber(10.0, 10, 2)
        num4 = TPNumber(0.0, 10, 2)
        with self.assertRaises(ValueError):
            result = num1 / num4
        del num1
        del num4

if __name__ == '__main__':
    unittest.main()