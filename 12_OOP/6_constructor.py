#12_OOP
#1_class_object
#6_constructor.py

class Bird:
    def __init__(self, name, size, color, food):
        self.name = name
        self.size = size
        self.color = color
        self.food = food

    def eat(self):
        print(self.name, "is eating", self.food)


crow = Bird("crow", 10, "black", "rice")
crow.eat()

eagle = Bird("eagle", 100, "gray", "mouse")
eagle.eat()
