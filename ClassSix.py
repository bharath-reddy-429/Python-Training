class Sample6:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def disp(self):
        print(self.a,self.b,self.c)
s=Sample6(100,200,300)
print(s.__dict__)
s.disp()