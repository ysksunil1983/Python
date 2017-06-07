class DyanmicPolyPract:
    def __init__(self):
        self.i = 1000
        print("in const of DyanmicPolyPract")
    def m1(self):
        print("in m1 function of DyanmicPolyPract")
class Test(DyanmicPolyPract):
    def __init__(self):
        super().__init__()
        self.j = 1100
        print("in const of Test")    
    def m1(self):
        super().m1()
        print("in m1 function of Test")

t1 = Test()
print(t1.j)
print(t1.i)
t1.m1()
