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
        print("I am an Employee, so i am breathing")

class programmer(Employee):
    company = "youtube"

    def getSalary(self):
        print("NO salary to programmers")

p= Person()
p.takeBreath()
#print(p.company)# throws error. no company in top class

e= Employee()
e.takeBreath()

pr=programmer()
pr.takeBreath() #prints takeBreath from employee class
print(pr.company) # prints company from Programmer class itself
print(pr.country)# prints country from Person class itself

