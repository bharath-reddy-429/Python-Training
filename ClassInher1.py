class Sample1:
    def getdata(self):
        self.a=10
        self.b=20
class Base(Sample1):
    def disp(self):
        print(self.a,self.b)
b=Base()
b.getdata()
b.disp()
