''' Create a class pets from a class animals and further create 
class Dog from pets. Add a method bark tp class Dog'''

class animals:
    animaltype = "Mammal"

class Pets:
    color = "White"
    
class dog:
    @staticmethod
    def bark():
        print("Bow Bow")

d= dog()
d.bark()
