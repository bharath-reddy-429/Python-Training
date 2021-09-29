class Parent:
    def getdata(self):
        self.a=100
        self.b=200
class Child(Parent):
    def getdata1(self):
        super().getdata()
        self.c=30
    def disp(self):
        print(self.a,self.b,self.c)
c=Child()
c.getdata1()
c.disp()