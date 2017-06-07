class X:
    def add(self,instanceOf, *args):
        if instanceOf == 'int':
            result = 0;
        if instanceOf == 'str':
            result = ' ';
        for i in args:
            result = result + i
        print(result);
x1= X()
x1.add('int',10,20,40,80);
x1.add('str','yellanki','sunil','kumar');
