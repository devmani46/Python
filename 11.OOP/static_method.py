class Employee:
    company ="Google"
    def getSalary(self): #if we remove self, it throws error
        print(F"salary of employee working in {self.company} is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning Sir")
    @staticmethod
    def time():
        print("The time is 9AM")

dev = Employee()
dev.salary = 10000 
dev.getSalary()

dev.greet()
dev.time()



