'''create a class programmer for storing infromation of few 
programmers working at microsoft '''


class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"the name of the {self.company} programmer is {self.name} and the product is {self.product}")


dev = Programmer("Dev", "Skype")
Alka = Programmer("Alka", "Github")
dev.getInfo()
Alka.getInfo()
