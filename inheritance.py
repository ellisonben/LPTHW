class Gran(object):

    def foo(self):
        print "This is Gran speaking"
    
    def bar(self):
        print "This is for Gran and all of her child classes multi-generational"
        
class Dad(Gran):

    def foo(self):
        print "This is Dad speaking"
    
    def boo(self):
        print "This is for Dad and all of his child classes"

class Mum(Gran):

    def boo(self):
        print "This is for Mum and all of her child classes"

class Son(Mum, Dad):

    def foo(self):
        print "This is Son speaking before super"
        super(Son, self).foo()
        print "This is Son speaking after super"


        
gran = Gran()
dad = Dad()
son = Son()

gran.foo()
dad.foo()
son.foo()

gran.bar()
dad.bar()
son.bar()

dad.boo()
son.boo()
