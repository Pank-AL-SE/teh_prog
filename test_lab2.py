import pytest
from lab2 import FOO

matrix1 = [[1,2,3,4,5,6,7,8,9],
           [11,12,13,14,15,16,17,18,19],
           [21,22,23,24,25,26,27,28,29]]
matrix2 = [[123,2345,567,90,2,3246,2],
           [52443,3544343,12312,357,759,11],
           [21,22,23,24,25,26,27,28,29]]

@pytest.mark.parametrize("a, b, c, fact",[(1,2,3,1),
                                         (5,1,10,1),
                                         (10,10,1,1)])
def test_lab2_1(a, b, c, fact):
    actual = FOO.foo1(a, b, c)
    assert  actual == fact

@pytest.mark.parametrize("v, fact",[(matrix1,210),
                                    (matrix2,3545530)])
def test_lab2_2(v,fact):
    actual = FOO.foo2(v)
    assert  actual == fact

@pytest.mark.parametrize("v, fact",[(matrix1,23),
                                    (matrix2,3544343)])
def test_lab2_3(v,fact):
    actual = FOO.foo3(v)
    assert  actual == fact