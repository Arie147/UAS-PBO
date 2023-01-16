class Parent:
    def __init__(self, name):
        self.name = name
    def display(self):
        print("Name:", self.name)

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def display(self):
        super().display()
        print("Age:", self.age)

p = Parent("Agus")
p.display()

c = Child("Sarah", 22)
c.display()