print("hello")
a=[1,2,3,4,5]
try:
    a[5]=100
    print(a)
except IndexError as e:
    print(e)