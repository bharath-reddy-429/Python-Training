a=int(input())
print("Before Exception")
try:
    if a>=18:
        print("Eligible for vote")
    else:
        raise  ValueError
except:
    print("Exception Block")
print("After Exception")