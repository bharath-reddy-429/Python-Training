class Parent:
    def getdata(self):
        self.a=100
        self.b=200
class Child(Parent):
    def getdata1(self):
        self.c=30
class SubChild(Child):
    def disp(self):
        print(self.a,self.b,self.c)
cc=SubChild()
cc.getdata()
cc.getdata1()
cc.disp()