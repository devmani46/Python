class Employee:
    company ="Google"
    name = "dev"
    def getSalary(self): #if we remove self, it throws error
        print(F"salary of {self.name} working in {self.company} is {self.salary}")

dev = Employee()
dev.salary = 10000 
dev.getSalary()
#Employee.getSalary(dev) #same as line 7


