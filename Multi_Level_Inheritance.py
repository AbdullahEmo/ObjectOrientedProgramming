class parent:#super class
    def config1(self):
        print("config 1")
    def config2(self):
        print("config 2")
class child(parent):#subclass # class child inherits parent
    def config3(self):
        print("config 3")
    def config4(self):
        print("config 4")
class grandchild(child): #class grandchild inherits child
    def config5(self):
        print("config 5")
""" it is called multi level inheritance because grandchild has parameter as child and
and child has parameter as parent so grandchild can access any of methods of any of classes above 
if we remove parent class from child than grandchild can only access to the child methods but cannot 
access to the parent methods  """


childd=child()
gchild=grandchild()
gchild.config5()
gchild.config3()
gchild.config1()
