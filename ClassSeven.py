class Sample7:
    def getdata(cls,a,b):
        cls.a=a;
        cls.b=b;
        print(a,b)
    def disp(self):
        print(Sample7.c)
s=Sample7()
s.getdata(100,200)
print(s.__dict__)
Sample7.c=100
print(Sample7.c)
s.disp()