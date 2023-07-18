class Employee:
    name = input("Enter Your Name : ")
    def variable(self):
        print(f"salary of {self.name} working in {self.company} is {self.salary}")

name = Employee()
name.company = input("Enter Your Company's name : ")
name.salary = int(input("Enter Your Salary : "))
 
name.variable()
#Employee.getSalary(dev) #same as line 7


