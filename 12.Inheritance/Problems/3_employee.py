''' Create a class Employee and add Salary and increment
properties to it. Write a method SalaryAferIncrement method with a @property
decorator with a setter which changes tge value of increment based on
the salary.'''

class Employee:
    salary = 1000
    increment = 2
    @property
    def SalaryAferIncrement(self):
        return self.salary*self.increment

    @SalaryAferIncrement.setter
    def SalaryAferIncrement(self, sai):
        increment = sai/self.salary

e= Employee()
print(e.SalaryAferIncrement)