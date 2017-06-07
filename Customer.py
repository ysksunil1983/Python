class InsufficientBalance(Exception):
    pass
class Customer:
    customerBankName = "SBI"
    def __init__(self,cname,cadd,cacno,cbal):
        self.cname =cname
        self.cadd= cadd
        self.cacno = cacno
        self.cbal = cbal
    def deposit(self, damt):
        self.cbal = self.cbal + damt
    def withdraw(self,wamt):
        if wamt > self.cbal:
            raise InsufficientBalance
        else:
            self.cbal = self.cbal - wamt
    def display(self):
        print (self.cname)
        print (self.cadd)
        print (self.cacno)
        print (self.cbal)
    def __str__(self):
        return self.cname + " "+self.cadd+ " "+ str(self.cacno)+" "+str(self.cbal)
        print (Customer.customerBankName)
c1 = Customer('sunil','tarnaka', 100001, 100000.00)
c2 = Customer('Mani','L B Nagar', 100003, 300000.00)
c3 = Customer('Santhosh','Nagole', 100002, 200000.00)

X = [c1,c2,c3]
for p in X:
    print(p)
print("After Sorting")
Y = sorted(X, key = lambda X : X.cbal,reverse = True)
for q in Y:
    print(q)
"""c1.display()
c1.deposit(10000.00)
try:
    c1.withdraw(50000.00)
except:
    print("insufficent amount")
c1.display()
try:
    c1.withdraw(70000.00)
except:
    print("insufficent amount")"""
