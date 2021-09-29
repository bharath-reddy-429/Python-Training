class Sample1:
    def getdata1(self):
        self.a=100
class Sample2:
    def __init__(self):
        self.b=200
class Child(Sample1, Sample2):
    def disp(self):
        super().getdata1()
        print(self.a,self.b)
c=Child()
c.disp()