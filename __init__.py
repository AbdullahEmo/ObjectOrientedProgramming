class Laptop():
    def __init__(self,RAM,CPU,HARDDISK):
        self.ram=RAM
        self.cpu=CPU
        self.harddisk=HARDDISK
    def capacity(self,comment):
        return "{},{},{}, {}".format(self.ram,self.cpu,self.harddisk,comment)

asus=Laptop('8GB','i5','1TB')
apple=Laptop('16 GB','i7','2TB')
print("Asus has " + asus.capacity("i'm not joking"))
print("Apple has " + apple.capacity("i'm not joking"))
