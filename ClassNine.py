class Sample9:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def disp(self):
        print(self.a,self.b)
    def getdata1(cls):
        cls.a=10
        cls.b=20
        print(cls.a, cls.b)
    def disp1(cls):
        print(cls.a,cls.b)
s=Sample9(1000,2000)
s.disp()
s.getdata1()
s.disp1()