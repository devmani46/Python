class Employee:
    company = "Google"
    eCode = 123

class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Programmer(Employee, Freelancer):
    name = "Dev"

p = Programmer()
p.upgradeLevel()
print(p.level)
print(p.company)   #prints Google because in class programmer, Employee is printed first

    
