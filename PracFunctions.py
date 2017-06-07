def f1(a=100):
    print(a);

f1(10);
def greet(name,msg='good Evening'):
    print("Hello",name,msg)
greet('sunil')
def f2(*x):
    print(type(x), id(x), x)
f2(10,20,20,20,50,'sunil')    
