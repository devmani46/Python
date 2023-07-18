''' Add a static method in pr 2 to
greet the user with hello'''

class Calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"the value of{self.number} square is {self.number **2}")

    def squareRoot(self):
        print(f"the value of{self.number} squareRoot is {self.number **0.5}")
 

    def cube(self):
        print(f"the value of{self.number} cube is {self.number **3}")

    @staticmethod
    def greet():
            print(f"Welcome to calculator")
a = Calculator(9)
a.greet()
a.square()
a.squareRoot()
a.cube()
