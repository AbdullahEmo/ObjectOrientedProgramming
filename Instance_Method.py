class car:
    company="Lamborghini"
    def __init__(self):
        self.name="Rambo Lambo"
    def get_name(self):
        return self.name
    #get_name is a instance method because it is pointed by self
car1=car()
print(car1.name)
