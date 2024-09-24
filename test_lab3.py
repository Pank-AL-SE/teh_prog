import pytest
from lab3 import FOO

@pytest.mark.parametrize("a, fact",[(12345,531),
                                    (None,None),
                                    (0,0)])
def test_lab3_1(a, fact):
    actual = FOO.foo1(a)
    assert  actual == fact

@pytest.mark.parametrize("a, fact",[(12345,4),
                                    (None,None),
                                    (1,None),
                                    (101,0),
                                    (-12345,4),])
def test_lab3_2(a, fact):
    actual = FOO.foo2(a)
    assert  actual == fact

@pytest.mark.parametrize("a,n, fact",[(123456,2,561234),
                                      (0,4,0),
                                      (None,4,None),
                                      (12345,0,12345),
                                      (-12345,2,-45123)])
def test_lab3_3(a,n, fact):
    actual = FOO.foo3(a,n)
    assert  actual == fact
