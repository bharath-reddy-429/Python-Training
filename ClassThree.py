class Sample3:
    def getdata(self,a,b):
        self.a=a
        self.b=b
    def disp(self):
        print(self.a,self.b)
s=Sample3()
s.getdata(100,200)
s.disp()
print(s.__dict__)
print("Instance Methods and Instance Variables")