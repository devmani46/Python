class Employee:
    company = "Google"
    salary= 100000
    salarybonus = 12345
    
    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter
    def totalSalary(self, val):
            self.salarybonus = val - self.salarybonus

e= Employee()
print(e.totalSalary) # to print from @property decorator
e.totalSalary = 1200000 #to change totalSalary
print(e.salary)
print(e.salarybonus) # to prnt from @totalSalary.setter 

