""" Create a class Person with attributes name and age. Add a method is_adult() that returns True if the person is 18 or older, otherwise False.
 """
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def is_adult(self):
        return self.age >= 18
p1 = Person("Taha",19)
print(p1.is_adult())