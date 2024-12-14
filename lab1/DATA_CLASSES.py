from dataclasses import dataclass

@dataclass
class DATA:
    non_decreasing_array = [56, 62, 65, 65, 83, 101, 404, 555, 70]
    decreasing_array = reversed(non_decreasing_array)
    random_array = [2, 55, 6, 8, 22, 6, 258, 65, 16, 9191, 8, 19, 6, 651, 653, 1, 974, 1]
    small_numbers_array = [1, 3, 5]
    big_numbers_array = [1000000000, 200000000, 3000000]
    very_small_numbers_array = [0.0000001, 0.000000005262]