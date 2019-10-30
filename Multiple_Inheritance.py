class parent:#super class
    def config1(self):
        print("config 1")
    def config2(self):
        print("config 2")
class child():#subclass
    def config3(self):
        print("config 3")
    def config4(self):
        print("config 4")
class grandchild(parent,child):
    def config5(self):
        print("config 5")
""" we can say class grandchild inherits both parent and child """

childd=child()
gchild=grandchild()
gchild.config5()
gchild.config3()
gchild.config1()
