import unittest
from main import TProc, TOprtn, TFunc

class TestTProc(unittest.TestCase):
    def setUp(self):
        self.processor = TProc()

    def test_reset_processor(self):
        self.processor.lop_res = 10
        self.processor.rop = 20
        self.processor.operation = TOprtn.ADD
        self.processor.reset_processor()
        self.assertIsNone(self.processor.lop_res)
        self.assertIsNone(self.processor.rop)
        self.assertEqual(self.processor.operation, TOprtn.NONE)

    def test_clear_operation(self):
        self.processor.operation = TOprtn.ADD
        self.processor.clear_operation()
        self.assertEqual(self.processor.operation, TOprtn.NONE)

    def test_run_operation_add(self):
        self.processor.lop_res = 2
        self.processor.rop = 3
        self.processor.operation = TOprtn.ADD
        self.processor.run_operation()
        self.assertEqual(self.processor.lop_res, 5)

    def test_run_operation_sub(self):
        self.processor.lop_res = 5
        self.processor.rop = 3
        self.processor.operation = TOprtn.SUB
        self.processor.run_operation()
        self.assertEqual(self.processor.lop_res, 2)

    def test_run_operation_mul(self):
        self.processor.lop_res = 2
        self.processor.rop = 3
        self.processor.operation = TOprtn.MUL
        self.processor.run_operation()
        self.assertEqual(self.processor.lop_res, 6)

    def test_run_operation_div(self):
        self.processor.lop_res = 6
        self.processor.rop = 3
        self.processor.operation = TOprtn.DIV
        self.processor.run_operation()
        self.assertEqual(self.processor.lop_res, 2)

    def test_run_function_rev(self):
        self.processor.rop = 2
        self.processor.run_function(TFunc.REV)
        self.assertEqual(self.processor.rop, 0.5)

    def test_run_function_sqr(self):
        self.processor.rop = 2
        self.processor.run_function(TFunc.SQR)
        self.assertEqual(self.processor.rop, 4)
    
    def test_invalid_1(self):
        self.processor.lop_res = 6
        self.processor.rop = '1'
        self.processor.operation = TOprtn.DIV
        with self.assertRaises(TypeError):
            self.processor.run_operation()
    
    def test_invalid_2(self):
        self.processor.lop_res = 6
        self.processor.rop = 0
        self.processor.operation = TOprtn.DIV
        with self.assertRaises(ValueError):
            self.processor.run_operation()

if __name__ == "__main__":
    unittest.main()