#Types of fun arguments
def fun1(a,b):
    return a-b
def fun2(b,a):
    return a-b
def fun3(a=100, b=200):
    return a+b
def fun4(a,b):
    return a+b
def fun5(a, b=200):
    return a+b
def fun6(*s):
    c=0
    for i in s:
        c+=i
    return c
def fun7(a, *s):
    c=0
    for i in s:
        c+=i
    return a+c
def fun8(**n):
    for i,j in n.items():
        print('variable {} and value {}'.format(i,j))

#we can return n number of values
def fun9(a,b):
    return a+b,a-b
print(fun1(100, 200))
print(fun2(100, 200))
print(fun3(10,20))
print(fun4(b=20,a=30))
print(fun5(b=300, a=100))
print(fun6(10,20,30,40))
print(fun7(10,20,30,40,50))
fun8(a=10,b=20,c=30,d=40)
sum,sub=fun9(100,200)
print(sum,sub)
