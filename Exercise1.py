a=int(input())
b=int(input())
c=int(input())
min=a if a>b and a>c else b if b>c else c
print('Minimum is : ',min)