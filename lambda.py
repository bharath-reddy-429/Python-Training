s=lambda a,b:a*b
print(s(4,5))

#big among three using lambda
s=lambda a,b,c: a if a>b and a>c else b if b>c else c
a,b,c=[int(x) for x in input().split()]
print(s(a,b,c))