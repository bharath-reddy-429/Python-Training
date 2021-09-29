#given number is prime or not
def Test(n):
    for i in range(2, n):
        if n%i==0:
            print("not Prime")
            break
    else:
        print("prime")
n=int(input())
Test(n)
