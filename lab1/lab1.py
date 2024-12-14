class FOO():

    def first_foo(v: list, ind: list) -> int:
        res = 1
        for i in ind:
            try:
                if v[i] > 0 and i < len(v) and i >= 0:
                    res *= v[i]
                else:
                    res = False
                    print(f'index out of the range {i}')
                    return res
            except:
                res = False
        return res
                

    def second_foo(mass: list[int]):
        return min(mass), mass.index(min(mass))

    def third_foo(mass: list[float]):
        return mass[::-1]