def fun(a,b,c):
    min=a if a>b and a>c else b if b>c else c
    return min
a,b,c=[int(x) for x in input().split()]
print(fun(a,b,c))
