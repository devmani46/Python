class Person:
    country ="Nepal"
    city = "Kathmandu"

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Google"

    def getSalary(self):
        print(f"Salary is {self.getSalary}")
    
    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee, so i am breathing")

class programmer(Employee):
    company = "youtube"

    def getSalary(self):
        print("NO salary to programmers")
        
    def takeBreath(self):
        super().takeBreath() #prints parents takebreath first and then yours
        print("I am an Programmer, so i am breathing ++")

p= Person()
p.takeBreath()

e= Employee()
e.takeBreath()

pr=programmer()
pr.takeBreath() 
