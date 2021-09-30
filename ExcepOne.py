a=10
try:
    print(a/0)
except ZeroDivisionError as e:
    print(e)