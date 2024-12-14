class FOO():
    def foo1(a: int, b: int, c: int):
        return min(a,b,c)
    
    def foo2(a: list[list[float]]):
        res = 0
        for i in range (len(a)):
            for j in range(len(a[i])):
                if (i+j) % 2 == 0:
                    res += a[i][j]
        return res
    
    def foo3(a: list[list[float]]):
        res = []
        for i in range(len(a)):
            for j in range(len(a[i])):
                if j<=i:
                    res.append(a[i][j])
        return max(res)