class Person:
    country ="Nepal"
    city = "Kathmandu"

    def __init__(self):
        print("\nIntializing Person ...\n")

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Google"

    def __init__(self):
        super().__init__()#prints parents super init
        print("Intializing Employee...\n")

    def getSalary(self):
        print(f"Salary is {self.getSalary}")
    
    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee, so i am breathing")

class programmer(Employee):
    company = "youtube"

    def getSalary(self):
        print("NO salary to programmers")

    def __init__(self):
        super().__init__()#prints parents super init
        print("Intializing Programmer...\n")
        
    def takeBreath(self):
        super().takeBreath() #prints parents takebreath first and then yours
        print("I am an Programmer, so i am breathing ++")


pr=programmer()
