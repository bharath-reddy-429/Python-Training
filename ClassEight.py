class Sample8:
    a=10
    def getdata(cls):
        cls.a=100
        print(cls.a)
    def disp(self):
        print(Sample8.a)
s=Sample8()
s.getdata()
s.disp()
