from enum import Enum


class TOprtn(Enum):
    NONE = 0
    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4


class TFunc(Enum):
    REV = 1
    SQR = 2


class TProc:
    def __init__(self):
        self._lop_res = None
        self._rop = None
        self._operation = TOprtn.NONE

    @property
    def lop_res(self):
        return self._lop_res

    @lop_res.setter
    def lop_res(self, value):
        self._lop_res = value

    @property
    def rop(self):
        return self._rop

    @rop.setter
    def rop(self, value):
        self._rop = value

    @property
    def operation(self):
        return self._operation

    @operation.setter
    def operation(self, value):
        self._operation = value

    def reset_processor(self):
        self._lop_res = None
        self._rop = None
        self._operation = TOprtn.NONE

    def clear_operation(self):
        self._operation = TOprtn.NONE

    def run_operation(self):
        if self.operation == TOprtn.ADD and isinstance(self._lop_res, type(self._rop)):
            self._lop_res = self._lop_res + self._rop
        elif self.operation == TOprtn.SUB and isinstance(self._lop_res, type(self._rop)):
            self._lop_res = self._lop_res - self._rop
        elif self.operation == TOprtn.MUL and isinstance(self._lop_res, type(self._rop)):
            self._lop_res = self._lop_res * self._rop
        elif self.operation == TOprtn.DIV and isinstance(self._lop_res, type(self._rop)):
            try:
                self._lop_res = self._lop_res / self._rop
            except ZeroDivisionError:
                raise ValueError("Деление на ноль")
        else:
            raise TypeError("invalid data")

    def run_function(self, func):
        if func == TFunc.REV:
            self._rop = 1 / self._rop
        elif func == TFunc.SQR:
            self._rop = self._rop ** 2