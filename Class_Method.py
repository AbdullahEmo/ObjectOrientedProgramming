class car:
    company="Lamborgini"
    def __init__(self):
        self.name="Rambo Lambo"
    @classmethod #for class method we need to bring classmethod decorator
    def class_method(cls):
        return cls.company

car1=car()
print(car.class_method())
