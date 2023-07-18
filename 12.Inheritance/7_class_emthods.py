class Employee:
    company = "Google"
    salary = 1000000
    location = "USA"

    def changeSalary(self, sal):
        self.salary= sal

    @classmethod 
    def changeSalary(cls, sal):
        cls.salary= sal
    

e = Employee()
print(e.salary) #to print default salary
e.changeSalary(455)
print(e.salary)  #to print changed salary
print(Employee.salary) #to print changed salary of class method



