''' Write a class Train which has methods to book a ticket, 
get staus(if no seats) and get fare information of trains
running under Railways'''

class Train:
    def __init__(self, name, fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"the name of the train is {self.name}")
        print(f"the seats availabe in the train is {self.seats}")

    def fareInfo(self):
        print(f"The price of the ticket is :Rs {self.fare}")
        
    def bookTicket(self):
        if(self.seats>0):
            print("Your Ticket has been booked")
            print(f"Your seat number is {self.seats}")
            self.seats= self.seats - 1
        else:
            print("Sorry! There are no available seats. This Train is booked")

intercity = Train("Intercity Express:12345", 90, 2)
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
