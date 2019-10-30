class parent:#super class
    def config1(self):
        print("config 1")
    def config2(self):
        print("config 2")
class child(parent):#subclass
    def config3(self):
        print("config 3")
    def config4(self):
        print("config 4")
# class child inherits parent
"""
child class can access any of the methods
from parent and child class, but when we we call
parent class u can not access any of methods from
other class except parent class
"""
childd=child()
parentt=parent()
parentt.config3()#it will not work
childd.config1()#it will work

#we can say this a single level inheritance
