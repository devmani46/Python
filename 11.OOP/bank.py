class BankForm:
    formType = "BankForm"
    def printData(self):
        print(f"name is {self.name}")
        print(f"account number is {self.account}")
        print(f"location is {self.location}")
    
form=BankForm()
form.name = (input("Enter your name : "))
form.account = int(input("Enter your account number : "))
form.location = (input("Enter your location : "))
form.printData()
