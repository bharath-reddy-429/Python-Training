class Sample10:
    c=50000
    def getdata(self):
        self.a=10
        self.b=20
        self.c=400
    def getdata1(cls):
        cls.a=100
        cls.b=200
        cls.c=300
    def getdata2():
        a=10
        b=20
        print(a,b)
    def disp(self):
        print(self.a,self.b,self.c)
    def disp1(cls):
        print(cls.a,cls.b,cls.c)
s=Sample10()
s.getdata()
s.disp()
s.getdata1()
Sample10.getdata2()
s.disp()
s.disp1()