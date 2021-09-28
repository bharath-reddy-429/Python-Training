#prime
from math import sqrt
n=int(input())
for j in range(2,n):
    for i in range(2,int(j/2)):
        if j%i==0 :
            break
    else:
        print(j,end=" ")
