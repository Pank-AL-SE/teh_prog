from PNumber import PNumber

class TPNumber(PNumber):
    def __sub__(self, other):
        if isinstance(other, TPNumber):
            if self.base != other.base or self.precision != other.precision:
                raise ValueError("Bases and precisions must match")
            result_value = self.number - other.number
            return TPNumber(result_value, self.base, self.precision)
        else:
            raise TypeError("Operand must be of type TPNumber")

    def __init__(self, value, base=10, precision=0):
        self.base = base
        self.precision = precision
        self.number_string = ""

        if type(value) is str:
            self._initialize_from_string(value, base, precision)
        elif isinstance(value, int) or isinstance(value, float):
            self._initialize_from_number(value, base, precision)
        else:
            raise TypeError("Unsupported type for value")

    def _initialize_from_string(self, value, base, precision):
        try:
            base_int = int(base)
            precision_int = int(precision)
        except ValueError:
            raise ValueError("Invalid base or precision string")

        if base_int < 2 or base_int > 16:
            raise ValueError("Base must be in the range [2..16]")
        if precision_int < 0:
            raise ValueError("Precision must be non-negative")

        self.base = base_int
        self.precision = precision_int
        self.number = self.StringToDouble(value, base_int)
        self.number_string = value

    def _initialize_from_number(self, value, base, precision):
        if base < 2 or base > 16:
            raise ValueError("Base must be in the range [2..16]")
        if precision < 0:
            raise ValueError("Precision must be non-negative")

        self.base = base
        self.precision = precision
        self.number = value
        self.number_string = self.ConvertToBase(value, base, precision)

    def ConvertToBase(self, value, base, precision):
        result = ""

        abs_value = abs(value)
        int_part = int(abs_value)
        frac_part = abs_value - int_part

        if int_part == 0:
            result = "0"
        else:
            while int_part > 0:
                digit = int_part % base
                result = ("0123456789ABCDEFG"[digit]) + result
                int_part //= base

        if precision > 0:
            result += "."
            while precision > 0:
                frac_part *= base
                digit = int(frac_part)
                frac_part -= digit
                result += ("0123456789ABCDEFG"[digit])
                precision -= 1

        if value < 0:
            result = "-" + result

        return result

    def StringToDouble(self, value, base):
        result = 0.0
        is_fraction = False
        fraction_multiplier = 1.0
        is_negative = (value[0] == "-")

        start_index = 1 if is_negative or value[0] == "+" else 0

        for i in range(start_index, len(value)):
            char = value[i]

            if char == ".":
                is_fraction = True
                continue

            upper_char = char.upper()

            if upper_char.isdigit():
                digit = ord(upper_char) - ord('0')
            elif 'A' <= upper_char <= 'F':
                digit = ord(upper_char) - ord('A') + 10
            else:
                raise ValueError("Invalid character in the number string")

            if digit >= base:
                raise ValueError("Digit out of range for the specified base")

            if is_fraction:
                fraction_multiplier /= base
                result += digit * fraction_multiplier
            else:
                result = result * base + digit

        return -result if is_negative else result

    def setBase(self, base):
        try:
            new_base = int(base)
            if new_base < 2 or new_base > 16:
                raise ValueError("Base must be between 2 and 16")
        except ValueError:
            raise ValueError("Invalid argument: the string is not a valid integer")

        self.base = new_base
        self.number_string = self.ConvertToBase(self.number, new_base, self.precision)

    
    def setPrecision(self, precision):
        try:
            new_precision = int(precision)
            if new_precision < 0:
                raise ValueError("Precision must be non-negative")
        except ValueError:
            raise ValueError("Invalid argument: the string is not a valid integer")
        self.precision = new_precision
        self.number_string = self.ConvertToBase(self.number, self.base, new_precision)

    
    def setPrecision(self, precision):
        if precision < 0:
            raise ValueError("Precision must be non-negative")
        self.precision = precision
        self.number_string = self.ConvertToBase(self.number, self.base, precision)

    
    def __del__(self):
        pass  # No need to implement destructor in Python

    def __repr__(self):
        return f"ПNumber({self.number}, {self.base}, {self.precision})"


tpnum = TPNumber(123.456, 8, 3)
print(tpnum.number_string)  # Должен вывести "173.340"