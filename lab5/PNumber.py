class PNumber():
    def __init__(self, value, base=10, precision=None):
        self.value = float(value)
        self.base = int(base)
        self.precision = int(precision) if precision is not None else None

    def __add__(self, other):
        if not isinstance(other, PNumber):
            raise TypeError("Operands must be of type PNumber")
        if self.base != other.base or self.precision != other.precision:
            raise ValueError("Bases and precisions must match")
        result_value = self.value + other.value
        return PNumber(result_value, self.base, self.precision)

    def __sub__(self, other):
        if not isinstance(other, PNumber):
            raise TypeError("Operands must be of type PNumber")
        if self.base != other.base or self.precision != other.precision:
            raise ValueError("Bases and precisions must match")
        result_value = self.value - other.value
        return PNumber(result_value, self.base, self.precision)

    def __mul__(self, other):
        if not isinstance(other, PNumber):
            raise TypeError("Operands must be of type PNumber")
        if self.base != other.base or self.precision != other.precision:
            raise ValueError("Bases and precisions must match")
        result_value = self.value * other.value
        return PNumber(result_value, self.base, self.precision)

    def __truediv__(self, other):
        if not isinstance(other, PNumber):
            raise TypeError("Operands must be of type PNumber")
        if self.base != other.base or self.precision != other.precision:
            raise ValueError("Bases and precisions must match")
        if other.value == 0.0:
            raise ZeroDivisionError("Division by zero")
        result_value = self.value / other.value
        return PNumber(result_value, self.base, self.precision)

    def Invert(self):
        if self.value == 0.0:
            raise ValueError("Cannot invert zero")
        result_value = 1.0 / self.value
        return PNumber(result_value, self.base, self.precision)

    def Square(self):
        result_value = self.value * self.value
        return PNumber(result_value, self.base, self.precision)

    def __repr__(self):
        return f"PNumber({self.value}, {self.base}, {self.precision})"


