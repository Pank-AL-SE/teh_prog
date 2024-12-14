import unittest

class ComplexNumberEditor:
    def __init__(self):
        self._string = "0, i* 0,"
        self.complexNumberIsZero = True

    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, a: str):
        self._string = a
        self.complexNumberIsZero = self._string == "0, i* 0,"

    def addDigit(self, a: int, check) -> str:
        if self.complexNumberIsZero:
            self._string = str(a) + ", i* 0,"
            self.complexNumberIsZero = False
            return self._string

        parts = self._string.split(", i* ")
        if len(parts) != 2:
            raise ValueError("Invalid complex number format")\

        if (a // 10) > 0:
            raise ValueError("Это чило а не цифра")
        if check == 'i':
            self._string = f"{parts[0]}, {str(a)}i* {parts[1]}"
        elif check == '1':
            self._string = f"{str(int(parts[0])+a)}, i* {parts[1]}"
        elif check == '2':
            self._string = f"{parts[0]}, {str(a)}i* {str(int(parts[1])+a)}"
        return self._string

    def addSign(self, sign: str, check = '2') -> str:
        if sign not in ["+", "-"]:
            raise ValueError("Invalid sign. Use '+' or '-'.")

        parts = self._string.split(", i* ")
        if len(parts) != 2:
            raise ValueError("Invalid complex number format")

        real, imag = parts[0], parts[1][:-1]  #remove trailing comma
        if check == '1':
            if real == "0":
                real = sign + "0"
            elif real[0] not in ["+", "-"]:
                real = sign + real
            else:
                real = sign + real[1:]
        else:
            if imag == "0":
                imag = sign + "0"
            elif imag[0] not in ["+", "-"]:
                imag = sign + imag
            else:
                imag = sign + imag[1:]


        self._string = f"{real}, i* {imag},"
        return self._string

    def addZero(self) -> str:
        if self.complexNumberIsZero:
            return self._string

        parts = self._string.split(", i* ")

        parts[0] += "0"  # Add zero to the real part
        self._string = ", i* ".join(parts) + ","
        return self._string


    def backspace(self) -> str:
        if self.complexNumberIsZero:
            return self._string

        self._string = self._string[:-1]
        if len(self._string) == 0:
            self._string = "0, i* 0,"
            self.complexNumberIsZero = True
        return self._string

    def clear(self) -> str:
        self._string = "0, i* 0,"
        self.complexNumberIsZero = True
        return self._string

    def edit(self, index: int) -> str:  #Corrected edit function
        if index < 0 or index >= len(self._string):
            raise IndexError("Index out of bounds")

        if self._string[index].isdigit():
            self._string = self._string[:index] + '0' + self._string[index+1:]

        return self._string


class TestComplexNumberEditor(unittest.TestCase):
    def test_addDigit(self):
        editor = ComplexNumberEditor()
        self.assertEqual(editor.addDigit(5,'1'), "5, i* 0,")
        self.assertEqual(editor.addDigit(2,'1'), "7, i* 0,")
        self.assertEqual(editor.addSign('+','2'), "7, i* +0,")


    def test_addSign(self):
        editor = ComplexNumberEditor()
        editor.addDigit(5,'2')
        self.assertEqual(editor.addSign("-",'2'), "5, i* -0,")

        editor.addDigit(2,'1')
        editor.addSign("-")
        self.assertEqual(editor.addSign("+",'1'), "+7, i* -0,")


    def test_addZero(self):
        editor = ComplexNumberEditor()
        editor.addDigit(5,'1')
        self.assertEqual(editor.addZero(), "50, i* 0,,")
        editor.clear()
        self.assertEqual(editor.addZero(), "0, i* 0,")

    def test_backspace(self):
        editor = ComplexNumberEditor()
        editor.addDigit(5,'1')
        self.assertEqual(editor.backspace(), "5, i* 0")
        editor.addDigit(5,'1')
        editor.addDigit(2,'1')
        self.assertEqual(editor.backspace(), "12, i* ")

    def test_clear(self):
        editor = ComplexNumberEditor()
        editor.addDigit(5,'1')
        self.assertEqual(editor.clear(), "0, i* 0,")
        self.assertEqual(editor.addSign('-','2'), "0, i* -0,")

    def test_edit(self):
        editor = ComplexNumberEditor()
        editor.addDigit(5,'1')
        self.assertEqual(editor.addSign('-','1'), "-5, i* 0,")
        self.assertEqual(editor.edit(0), "-5, i* 0,")
        self.assertEqual(editor.addSign('-','2'), "-5, i* -0,")
        editor.addDigit(5,'1')
        editor.addDigit(2,'1')
        self.assertEqual(editor.edit(1), "2, i* -0,")

    def test_complexNumberIsZero(self):
        editor = ComplexNumberEditor()
        self.assertTrue(editor.complexNumberIsZero)
        editor.addDigit(1,'1')
        self.assertFalse(editor.complexNumberIsZero)
        editor.clear()
        self.assertTrue(editor.complexNumberIsZero)

    def test_invalid_sign(self):
        editor = ComplexNumberEditor()
        with self.assertRaises(ValueError):
            editor.addSign("x")

    def test_invalid_complex_number_format(self):
        editor = ComplexNumberEditor()
        editor._string = "1+2"
        with self.assertRaises(ValueError):
            editor.addSign("-")      

    def setUp(self):
        self.editor = ComplexNumberEditor()
            
    def test_add_sign_invalid_sign(self):
        with self.assertRaises(ValueError):
            self.editor.addSign('*')
            
    def test_backspace_empty_string(self):
        self.editor.clear()
        result = self.editor.backspace()
        self.assertEqual(result, "0, i* 0,")
        
    def test_edit_out_of_bounds(self):
        with self.assertRaises(IndexError):
            self.editor.edit(-1)
        with self.assertRaises(IndexError):
            self.editor.edit(100)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
