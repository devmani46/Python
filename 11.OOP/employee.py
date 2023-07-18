class Employee:
    company = "Google"

dev = Employee()
dev.salary = 10000
dev.address = "panga"

asd = Employee()
asd.salary = 20000
asd.address = "Kirtipur"

print(dev.company)
print(asd.company)

Employee.company = "Youtube"
print(dev.company)
print(asd.company)

print(dev.salary)
print(asd.salary)

print(dev.address)
print(asd.address)