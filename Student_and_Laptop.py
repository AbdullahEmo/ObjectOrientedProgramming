class Student:
    University="Leading University"
    def __init__(self,name,age,batch):
        self.name=name
        self.age=age
        self.batch=batch
        self.lap=self.Laptop(input("Brand:"),int(input("RAM:")),input("CPU:"))
#here self is a pointer so we can say Emon==self
    def show(self):
        print("{0} age is {1} and batch {2}".format(self.name,self.age,self.batch))
        self.lap.show()
    class Laptop:
        def __init__(self,brand,ram,cpu):
            self.brand=brand
            self.ram=ram
            self.cpu=cpu
        def show(self):
            print("{} ram {} and cpu {}".format(self.brand,self.ram,self.cpu))

i=0
while i<3:
    Emon=Student(input("name:"),int(input("age:")),input("Batch:"))
    Emon.show()
    print(Student.University)
    i+=1
