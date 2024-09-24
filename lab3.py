class FOO():
    
    def foo1(a: int):
        b = ''
        try:
            a = str(a)
        except:
            assert False
        for i, val in enumerate(a):
            if (i+1) % 2 == 1:
                b+=val
            else:
                continue

        try:
            b = int(b[::-1])
        except:
            b = None
        return b
    
    def foo2(a):
        maxc = 0
        flag = False
        if a != None:
            a = str(abs(a))
        else:
            return None
        for i, val in enumerate(a):
            if (i+1) % 2 == 0:
                maxc=max(maxc,int(val))
                flag = True
            else:
                continue
        return maxc if flag == True else None
    
    def foo3(a,n):
        flag = False
        if a != None:
            if a<0:
                flag = True
            a = str(abs(a))
        else:
            return None
        for i in range(n):
            a = a[-1:]+a[:-1]
        try:
            a = int(a)
        except:
            a = None
        return a if flag == False else -a
        
