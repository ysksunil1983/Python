a =[10,20,30,40,50]
print(a,type(a),id(a))
a.append(60)
print(a,type(a),id(a))
a.insert(0,5)
print(a,type(a),id(a))
print(a)
b = ['abcd','efgh','ijkl']
print(b)
a.extend(b)
print(a)
print(a.index('abcd'))
a.remove(5)
print(a)
a.sort()
a.reverse()
print(a)
a.pop()
print(a)
a.pop(5)
print(a)
