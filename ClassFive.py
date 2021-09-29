class Sample5:
    def getdata(self):
        self.a=100
        self.b=200
    def disp(self):
        print(self.a,self.b,self.c)
s=Sample5()
s.getdata()
s.c=30
s.disp()
print(s.a)
