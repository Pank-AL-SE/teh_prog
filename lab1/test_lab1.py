import pytest
from lab1 import FOO as f
import DATA_CLASSES

non_decreasing_array = [56, 62, 65, 65, 83, 101, 404, 555]
decreasing_array = non_decreasing_array[::-1]
random_array = [2, 55, 6, 8, 22, 6, 258, 65, 16, 9191, 8, 19, 6, 651, 653, 1, 974, 1]
small_numbers_array = [1, 3, 5]
big_numbers_array = [1000000000, 200000000, 3000000]
very_small_numbers_array = [0.0000001, 0.000000005262]

@pytest.mark.parametrize("v, ind, fact",[(non_decreasing_array, [1,2,3], 261950),
                                         (random_array, [2,3,5], 288),
                                         (random_array, [2,20,5], False),
                                         (big_numbers_array, [1,2], 600000000000000),
                                         (random_array, [2,-1,5], False)])
def test_1(v,ind,fact):
    actual = f.first_foo(v,ind)
    assert  actual == fact

@pytest.mark.parametrize("v, fact_min, fact_ind",[(non_decreasing_array,56,0),
                                                   (decreasing_array, 56, len(non_decreasing_array)-1),
                                                   (random_array, 1, 15)])
def test_2(v, fact_min, fact_ind):    
    actual_min, actual_ind =  f.second_foo(v)
    assert actual_min == fact_min
    assert actual_ind == fact_ind

@pytest.mark.parametrize("v, fact",[(non_decreasing_array, non_decreasing_array[::-1]),
                                    (decreasing_array, decreasing_array[::-1]),
                                    (random_array, random_array[::-1])])
def test_3(v, fact):    
    actual = f.third_foo(v)
    assert actual == fact
